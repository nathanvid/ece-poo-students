import os
import subprocess
import sys
import tomllib

import pytest


@pytest.fixture
def project_dir(code_dir):
    return code_dir / "04_modules_package" / "ticketing"


@pytest.fixture
def ticketing(project_dir, monkeypatch):
    """Import the package from its src/ folder, as an installed package would be."""
    monkeypatch.syspath_prepend(str(project_dir / "src"))
    for name in list(sys.modules):
        if name == "ticketing" or name.startswith("ticketing."):
            monkeypatch.delitem(sys.modules, name)
    import ticketing

    return ticketing


@pytest.fixture
def pyproject(project_dir):
    with open(project_dir / "pyproject.toml", "rb") as file:
        return tomllib.load(file)


# --- pyproject.toml ----------------------------------------------------------------


def test_project_table(pyproject):
    project = pyproject["project"]
    assert project["name"] == "ticketing"
    assert project["version"] == "0.1.0"
    assert project.get("description", "") != ""
    assert project.get("readme") == "README.md"
    assert project.get("requires-python") == ">=3.12"
    assert project.get("dependencies") == []


def test_command(pyproject):
    scripts = pyproject["project"].get("scripts", {})
    assert scripts == {"ticketing": "ticketing.cli:main"}


def test_build_system(pyproject):
    build = pyproject.get("build-system", {})
    assert build.get("requires") == ["hatchling"]
    assert build.get("build-backend") == "hatchling.build"


# --- the package -------------------------------------------------------------------


def test_package_offers(ticketing):
    assert ticketing.__version__ == "0.1.0"
    assert ticketing.Cart.__module__ == "ticketing.cart"
    assert ticketing.price_of("full") == 22.0
    assert ticketing.PRICES["child"] == 8.0


def test_cart(ticketing):
    cart = ticketing.Cart()
    assert cart.count() == 0
    assert cart.total() == 0.0
    assert cart.lines() == []
    cart.add("full", 2)
    cart.add("child")
    cart.add("full")
    assert cart.count() == 4
    assert cart.total() == 3 * 22.0 + 8.0 + 1.5
    assert cart.lines() == ["3 x full", "1 x child"]


def test_cart_errors(ticketing):
    cart = ticketing.Cart()
    with pytest.raises(ValueError, match="Unknown category: vip."):
        cart.add("vip")
    with pytest.raises(ValueError, match="Invalid count: 0."):
        cart.add("full", 0)
    assert cart.count() == 0


def run_cli(project_dir, *arguments):
    env = dict(os.environ, PYTHONPATH=str(project_dir / "src"), PYTHONUTF8="1")
    return subprocess.run(
        [sys.executable, "-m", "ticketing.cli", *arguments],
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=env,
        timeout=10,
    )


def test_command_line(project_dir):
    result = run_cli(project_dir, "full", "reduced", "child", "child")
    assert result.returncode == 0, result.stderr
    assert result.stdout.splitlines() == [
        "1 x full",
        "1 x reduced",
        "2 x child",
        "Total: 51.50 EUR",
    ]
    wrong = run_cli(project_dir, "vip")
    assert wrong.returncode == 1
    assert "Error: Unknown category: vip." in wrong.stdout
