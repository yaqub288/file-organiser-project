from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parent


def main() -> None:
    if not shutil.which("pyinstaller") and not _module_available("PyInstaller"):
        raise SystemExit(
            "PyInstaller is not installed. Install it with: python -m pip install pyinstaller"
        )

    subprocess.run(
        [
            sys.executable,
            "-m",
            "PyInstaller",
            "--noconfirm",
            "--clean",
            "--onefile",
            "--windowed",
            "--name",
            "FileOrganiser",
            str(ROOT / "main.py"),
        ],
        cwd=ROOT,
        check=True,
    )
    print(f"Built distributable in: {ROOT / 'dist'}")


def _module_available(name: str) -> bool:
    try:
        __import__(name)
    except ImportError:
        return False
    return True


if __name__ == "__main__":
    main()
