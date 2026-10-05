import json
from inspect import isabstract

import pytest


@pytest.fixture
def notifier(load_exercise):
    return load_exercise("03_abstract_classes/notifier.py")


@pytest.fixture
def storage(load_exercise):
    return load_exercise("03_abstract_classes/storage.py")


# --- notifier ----------------------------------------------------------------------


def test_notifier_is_abstract(notifier):
    assert isabstract(notifier.Notifier)
    with pytest.raises(TypeError):
        notifier.Notifier()


def test_print_notifier(notifier, capsys):
    sms = notifier.PrintNotifier("SMS")
    assert isinstance(sms, notifier.Notifier)
    sms.send_all(["Doors open", "Show starts"])
    assert capsys.readouterr().out == "[SMS] Doors open\n[SMS] Show starts\n"


def test_memory_notifier_and_broadcast(notifier, capsys):
    first = notifier.MemoryNotifier()
    second = notifier.MemoryNotifier()
    assert first.sent == []
    notifier.broadcast([first, notifier.PrintNotifier("Mail"), second], "Hello")
    assert first.sent == ["Hello"]
    assert second.sent == ["Hello"]
    assert capsys.readouterr().out == "[Mail] Hello\n"


# --- storage -----------------------------------------------------------------------

SHOWS = [
    {
        "title": "Late Laughs",
        "artist": "Nora Lebrun",
        "venue": "Le Kiosque",
        "start": "2027-06-11T23:30",
        "duration": 60,
        "price": 12.0,
    },
    {
        "title": "Tall Tales",
        "artist": "Léa Fontaine",
        "venue": "Théâtre des Planches",
        "start": "2027-06-11T20:30",
        "duration": 80,
        "price": 28.0,
    },
]


def test_storage_is_abstract(storage):
    assert isabstract(storage.ProgrammeStorage)
    with pytest.raises(TypeError):
        storage.ProgrammeStorage()
    assert issubclass(storage.StorageError, Exception)


@pytest.mark.parametrize("kind", ["MemoryStorage", "JsonStorage", "CsvStorage"])
def test_follows_the_interface(storage, kind):
    assert issubclass(getattr(storage, kind), storage.ProgrammeStorage)
    assert not isabstract(getattr(storage, kind))


def test_memory_storage(storage):
    memory = storage.MemoryStorage()
    assert memory.load() == []
    memory.save(SHOWS)
    assert memory.load() == SHOWS
    assert memory.count() == 2
    assert storage.MemoryStorage(SHOWS).count() == 2


def test_memory_storage_keeps_copies(storage):
    shows = [dict(SHOWS[0])]
    memory = storage.MemoryStorage(shows)
    shows[0]["title"] = "Changed outside"
    memory.load()[0]["title"] = "Changed outside"
    memory.load().append({})
    assert memory.load() == [SHOWS[0]]


def test_json_storage(storage, tmp_path):
    path = tmp_path / "data" / "programme.json"
    json_storage = storage.JsonStorage(path)
    json_storage.save(SHOWS)
    assert "Théâtre des Planches" in path.read_text(encoding="utf-8")
    assert storage.JsonStorage(path).load() == SHOWS
    assert json_storage.count() == 2


def test_json_storage_errors(storage, tmp_path):
    path = tmp_path / "programme.json"
    with pytest.raises(storage.StorageError, match="programme.json does not exist."):
        storage.JsonStorage(path).load()
    path.write_text("[{", encoding="utf-8")
    with pytest.raises(storage.StorageError, match="is not valid JSON."):
        storage.JsonStorage(path).load()
    path.write_text(json.dumps({"title": "Gala"}), encoding="utf-8")
    with pytest.raises(storage.StorageError, match="must hold a list of shows."):
        storage.JsonStorage(path).load()


def test_json_error_keeps_its_cause(storage, tmp_path):
    path = tmp_path / "programme.json"
    path.write_text("[{", encoding="utf-8")
    with pytest.raises(storage.StorageError) as error:
        storage.JsonStorage(path).load()
    assert isinstance(error.value.__cause__, json.JSONDecodeError), "Use `from error`."


def test_copy_programme(storage, tmp_path):
    source = storage.MemoryStorage(SHOWS)
    target = storage.JsonStorage(tmp_path / "copy.json")
    assert storage.copy_programme(source, target) == 2
    assert target.load() == SHOWS


def test_csv_storage(storage, tmp_path):
    """[ext.]"""
    path = tmp_path / "programme.csv"
    csv_storage = storage.CsvStorage(path)
    csv_storage.save(SHOWS)
    assert path.read_text(encoding="utf-8").splitlines()[0] == (
        "title,artist,venue,start,duration,price"
    )
    assert csv_storage.load() == SHOWS
    with pytest.raises(storage.StorageError):
        storage.CsvStorage(tmp_path / "missing.csv").load()
