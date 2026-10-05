from pathlib import Path

import nbformat
import pytest
from fastapi.testclient import TestClient
from nbclient import NotebookClient

from checks import load_module

EXAMPLES_DIR = Path(__file__).parent.parent / "examples"


@pytest.mark.parametrize(
    "example", sorted(p.name for p in EXAMPLES_DIR.glob("*.ipynb"))
)
def test_example_notebook_runs(example, tmp_path):
    notebook = nbformat.read(EXAMPLES_DIR / example, as_version=4)
    NotebookClient(notebook, timeout=30, kernel_name="python3").execute(
        cwd=str(tmp_path)
    )


def test_example_hello_api():
    client = TestClient(load_module(EXAMPLES_DIR / "hello_api.py").app)
    assert client.get("/venues", params={"min_capacity": 200}).json()[0]["slug"] == (
        "grand-casino"
    )
    assert client.get("/venues/nowhere").status_code == 404
