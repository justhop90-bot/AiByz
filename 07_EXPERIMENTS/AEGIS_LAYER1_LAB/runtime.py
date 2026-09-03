import os
import subprocess
from pathlib import Path
from datetime import datetime, timezone


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def launch(experiment, command, run_dir, timeout):
    directory = Path(run_dir)
    directory.mkdir(parents=True, exist_ok=True)
    manifest = directory / "experiment.json"
    manifest.write_text(__import__('json').dumps(experiment, indent=2), encoding="utf-8")
    env = os.environ.copy()
    env["AEGIS_EXPERIMENT_ID"] = experiment["experiment_id"]
    env["AEGIS_EXPERIMENT_JSON"] = str(manifest)
    started = utc_now()
    process = subprocess.Popen(command, cwd=directory, env=env,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               text=True)
    try:
        stdout, stderr = process.communicate(timeout=timeout)
        status = "completed"
    except subprocess.TimeoutExpired:
        process.kill()
        stdout, stderr = process.communicate()
        status = "timeout"
    return {
        "experiment_id": experiment["experiment_id"],
        "started_at": started,
        "finished_at": utc_now(),
        "exit_code": process.returncode,
        "stdout": stdout,
        "stderr": stderr,
        "status": status,
    }
