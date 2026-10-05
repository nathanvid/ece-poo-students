import sys
import tomllib
from pathlib import Path

import nbformat
import pytest
from nbclient import NotebookClient

EXAMPLES_DIR = Path(__file__).parent.parent / "examples"
GREETINGS_DIR = EXAMPLES_DIR / "greetings"


@pytest.mark.parametrize(
    "example", sorted(p.name for p in EXAMPLES_DIR.glob("*.ipynb"))
)
def test_example_notebook_runs(example, tmp_path):
    notebook = nbformat.read(EXAMPLES_DIR / example, as_version=4)
    NotebookClient(notebook, timeout=30, kernel_name="python3").execute(
        cwd=str(tmp_path)
    )


def test_greetings_package(monkeypatch):
    monkeypatch.syspath_prepend(str(GREETINGS_DIR / "src"))
    for name in list(sys.modules):
        if name.startswith("greetings"):
            monkeypatch.delitem(sys.modules, name)
    import greetings

    assert greetings.greet("Nora") == "Hello Nora."
    assert greetings.greet("Nora", excited=True) == "Hello Nora!"

    with open(GREETINGS_DIR / "pyproject.toml", "rb") as file:
        project = tomllib.load(file)["project"]
    assert project["scripts"] == {"greet": "greetings.cli:main"}
