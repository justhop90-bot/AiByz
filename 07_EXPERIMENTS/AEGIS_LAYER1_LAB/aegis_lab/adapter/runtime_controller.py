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


class AoE2DERuntime:
    """Launch only a verified build with an argv list and isolated cwd."""

    def __init__(self, executable: str, expected_sha256: str) -> None:
        self.executable = executable
        self.expected_sha256 = expected_sha256

    def verify(self) -> BuildIdentity:
        return verify_executable(self.executable, self.expected_sha256)

    def launch(
        self,
        run_dir: str,
        extra_args: list[str] | None = None,
        timeout_seconds: int = 120,
    ) -> RuntimeResult:
        """Run the verified executable; never invoke through a shell."""
        identity = self.verify()
        directory = Path(run_dir).resolve()
        directory.mkdir(parents=True, exist_ok=True)
        stdout_path = directory / "process.stdout.txt"
        stderr_path = directory / "process.stderr.txt"
        argv = [identity.path, *(extra_args or [])]
        started = time.monotonic()
        env = os.environ.copy()
        env["AEGIS_BUILD_SHA256"] = identity.sha256

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
