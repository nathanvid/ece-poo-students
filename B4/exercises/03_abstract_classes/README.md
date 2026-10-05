# 03 - Abstract classes

Check: `uv run pytest B4 -k abstract`

## notifier.py `[core]`

`Notifier` is abstract (`send` is already declared abstract). Write:

- `send_all(messages)` in `Notifier`: calls `send` for each message;
- `PrintNotifier(prefix)`: `send("Doors open")` prints `[SMS] Doors open`;
- `MemoryNotifier()`: keeps the messages in the list `sent`;
- `broadcast(notifiers, message)`: sends the message with each notifier.

## storage.py `[core]`

The programme is a list of shows (dicts). `ProgrammeStorage` is the
interface: `load()` and `save(shows)` are abstract, `count()` uses `load()`.

| Class                       | Keeps the shows                                                                                               |
| --------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `MemoryStorage(shows=None)` | in a private list. `load` gives copies, `save` stores copies: changing a dict outside changes nothing inside. |
| `JsonStorage(path)`         | in a UTF-8 JSON file; `save` creates the folder if needed                                                     |
| `CsvStorage(path)` `[ext.]` | in a CSV file, columns of `FIELDS`; `duration` and `price` converted back into numbers                        |

`JsonStorage.load` raises `StorageError`, the exception of the module:

- `programme.json does not exist.`
- `programme.json is not valid JSON.`, raised `from` the `JSONDecodeError`;
- `programme.json must hold a list of shows.`

`copy_programme(source, target)` saves the shows of any storage into any other
one, and returns how many.

Hint: `dict(show)` makes a copy of a dict.
