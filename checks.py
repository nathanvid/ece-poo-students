"""Helpers used by the tests of every block."""

import importlib.util
import os
import subprocess
import sys
from pathlib import Path
from types import ModuleType


def run_python(path: Path, stdin: str = "") -> subprocess.CompletedProcess:
    """Run a Python file, type `stdin` for it, capture what it prints.

    UTF-8 is forced on both sides so that accented text ("Théâtre") behaves the
    same on Windows, macOS and Linux, whatever the system language.
    """
    env = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8")
    return subprocess.run(
        [sys.executable, str(path)],
        input=stdin,
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=env,
        timeout=10,
    )


def lines(*answers: str) -> str:
    """Join the answers typed by the user, one per line."""
    return "\n".join(answers) + "\n"


def assert_in_order(output: str, *expected: str) -> None:
    """Check that each expected text appears in `output`, in this order."""
    position = 0
    for text in expected:
        found = output.find(text, position)
        assert found != -1, f"{text!r} not found (in order) in:\n{output}"
        position = found + len(text)


def load_module(path: Path) -> ModuleType:
    """Import a Python file as a module, without running its `main()`."""
    # A name of its own, registered like a normal import (dataclasses need it).
    name = f"exercise_{path.parent.name}_{path.stem}"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module
