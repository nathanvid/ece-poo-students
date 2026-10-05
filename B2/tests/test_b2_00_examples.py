import shutil
from pathlib import Path

import nbformat
import pytest
from nbclient import NotebookClient

from checks import run_python

EXAMPLES_DIR = Path(__file__).parent.parent / "examples"


def test_traceback_demo_crashes_as_expected():
    result = run_python(EXAMPLES_DIR / "traceback_demo.py")
    assert result.returncode != 0
    assert "KeyError: 'duration'" in result.stderr


@pytest.mark.parametrize(
    "example", sorted(p.name for p in EXAMPLES_DIR.glob("*.ipynb"))
)
def test_example_notebook_runs(example, tmp_path):
    # Run in a copy, so that the files written by the notebook stay out of
    # the course folder.
    shutil.copytree(EXAMPLES_DIR / "data", tmp_path / "data")
    notebook = nbformat.read(EXAMPLES_DIR / example, as_version=4)
    NotebookClient(notebook, timeout=30, kernel_name="python3").execute(
        cwd=str(tmp_path)
    )
