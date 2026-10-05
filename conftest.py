"""Test helpers shared by every block."""

import shutil
from pathlib import Path
from types import ModuleType

import pytest

from checks import load_module, run_python


def pytest_addoption(parser):
    parser.addoption(
        "--code-dir",
        default=None,
        help="Folder holding B1..B5 code to test instead of the exercises.",
    )


@pytest.fixture
def code_dir(request) -> Path:
    """Folder containing the scripts under test, e.g. B1/exercises."""
    bloc_dir = request.path.parent.parent
    option = request.config.getoption("--code-dir")
    if option is None:
        return bloc_dir / "exercises"
    return request.config.rootpath / option / bloc_dir.name


@pytest.fixture
def run_script(code_dir):
    """Run a script of the folder under test and return what it prints."""

    def run(filename: str, stdin: str = "") -> str:
        result = run_python(code_dir / filename, stdin)
        assert result.returncode == 0, f"{filename} crashed:\n{result.stderr}"
        return result.stdout

    return run


@pytest.fixture
def load_exercise(code_dir):
    """Import an exercise file to call its functions, e.g. timing.to_clock(90)."""

    def load(filename: str) -> ModuleType:
        try:
            return load_module(code_dir / filename)
        except OSError:
            pytest.fail(
                f"{filename} asks a question as soon as it is imported. "
                'Put that code in main(), under if __name__ == "__main__":'
            )

    return load


@pytest.fixture
def exercise_copy(request, code_dir, tmp_path):
    """Copy an exercise folder, data files included, to a temporary folder.

    The program can then create and change files there without touching the
    real ones.
    """

    def copy(folder: str) -> Path:
        target = tmp_path / folder
        exercises_dir = request.path.parent.parent / "exercises"
        shutil.copytree(exercises_dir / folder, target)
        for script in (code_dir / folder).glob("*.py"):
            shutil.copy(script, target / script.name)
        return target

    return copy
