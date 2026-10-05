from pathlib import Path

import nbformat
import pytest
from nbclient import NotebookClient

EXAMPLES_DIR = Path(__file__).parent.parent / "examples"


@pytest.mark.parametrize(
    "example", sorted(p.name for p in EXAMPLES_DIR.glob("*.ipynb"))
)
def test_example_notebook_runs(example, tmp_path):
    notebook = nbformat.read(EXAMPLES_DIR / example, as_version=4)
    NotebookClient(notebook, timeout=30, kernel_name="python3").execute(
        cwd=str(tmp_path)
    )
