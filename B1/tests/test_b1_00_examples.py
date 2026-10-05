from pathlib import Path

import nbformat
import pytest
from nbclient import NotebookClient

from checks import lines, run_python

EXAMPLES_DIR = Path(__file__).parent.parent / "examples"

INPUTS = {
    "04_input_output.py": lines(
        "Lina", "19", "2", "3", "1.72", "0", "180", "2", " YES "
    ),
}


@pytest.mark.parametrize("example", sorted(p.name for p in EXAMPLES_DIR.glob("*.py")))
def test_example_script_runs(example):
    result = run_python(EXAMPLES_DIR / example, INPUTS.get(example, ""))
    assert result.returncode == 0, result.stderr


@pytest.mark.parametrize(
    "example", sorted(p.name for p in EXAMPLES_DIR.glob("*.ipynb"))
)
def test_example_notebook_runs(example):
    notebook = nbformat.read(EXAMPLES_DIR / example, as_version=4)
    NotebookClient(notebook, timeout=30, kernel_name="python3").execute()
