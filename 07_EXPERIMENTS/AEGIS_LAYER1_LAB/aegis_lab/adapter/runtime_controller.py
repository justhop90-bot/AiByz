"""Controlled process lifecycle for native AoE2DE experiments.

This module deliberately does not pretend that launching the executable is
sufficient to create a causal experiment. Scenario setup, observation, and
adjudication remain explicit stages.
"""
from __future__ import annotations

import os
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path

from .build_guard import BuildIdentity, verify_executable


@dataclass(frozen=True)
class RuntimeResult:
    status: str
    pid: int | None
    returncode: int | None
    stdout_path: str
    stderr_path: str
    duration_seconds: float


SAFE_ENVIRONMENT_KEYS = frozenset({
    "APPDATA", "LOCALAPPDATA", "PROGRAMDATA", "PROGRAMFILES",
    "PROGRAMFILES(X86)", "SYSTEMDRIVE", "SYSTEMROOT", "TEMP", "TMP",
    "USERPROFILE", "PATH", "WINDIR",
})


class AoE2DERuntime:
    """Launch only a verified build inside the isolated AEGIS lab root."""

    def __init__(self, executable: str, expected_sha256: str,
                 run_root: str | None = None) -> None:
        self.executable = executable
        self.expected_sha256 = expected_sha256
        default_root = Path(__file__).resolve().parents[2] / "runs"
        self.run_root = Path(run_root).resolve() if run_root else default_root

    def verify(self) -> BuildIdentity:
        return verify_executable(self.executable, self.expected_sha256)

    def _validate_run_directory(self, run_dir: str) -> Path:
        root = self.run_root.resolve()
        directory = Path(run_dir).resolve()
        if directory == root or root not in directory.parents:
            raise ValueError(f"run directory escapes lab root: {directory}")
        return directory

    @staticmethod
    def _sanitized_environment(build_sha256: str) -> dict[str, str]:
        env = {key: value for key, value in os.environ.items()
               if key.upper() in SAFE_ENVIRONMENT_KEYS}
        env["AEGIS_BUILD_SHA256"] = build_sha256
        return env

    def launch(
        self,
        run_dir: str,
        extra_args: list[str] | None = None,
        timeout_seconds: int = 120,
    ) -> RuntimeResult:
        """Run the verified executable; never invoke through a shell."""
        if timeout_seconds <= 0:
            raise ValueError("timeout_seconds must be positive")
        identity = self.verify()
        directory = self._validate_run_directory(run_dir)
        directory.mkdir(parents=True, exist_ok=True)
        stdout_path = directory / "process.stdout.txt"
        stderr_path = directory / "process.stderr.txt"
        argv = [identity.path, *(extra_args or [])]
        started = time.monotonic()
        env = self._sanitized_environment(identity.sha256)

        with stdout_path.open("w", encoding="utf-8", errors="replace") as stdout:
            with stderr_path.open("w", encoding="utf-8", errors="replace") as stderr:
                process = subprocess.Popen(
                    argv,
                    cwd=directory,
                    env=env,
                    stdout=stdout,
                    stderr=stderr,
                    shell=False,
                )
                try:
                    code = process.wait(timeout=timeout_seconds)
                    status = "completed"
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait(timeout=10)
                    code = process.returncode
                    status = "timeout"

        return RuntimeResult(
            status=status,
            pid=process.pid,
            returncode=code,
            stdout_path=str(stdout_path),
            stderr_path=str(stderr_path),
            duration_seconds=time.monotonic() - started,
        )
