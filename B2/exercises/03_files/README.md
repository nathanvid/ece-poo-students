# 03 - Files

Check: `uv run pytest B2 -k files`

Always open files with `encoding="utf-8"`, and CSV files with `newline=""`
too.

## line_stats.py `[core]`

`file_stats(path)` reads a text file and returns a dict:

```python
{
    "lines": 6,
    "words": 41,
    "longest": "Four venues, four days, and a sea breeze between two shows.",
}
```

Empty lines count as lines. `"longest"` is the longest line without its `\n`
(the first one if two lines have the same length). A missing file raises
`FileNotFoundError`: nothing to do, `open` already does it.

`number_lines(source, target)` copies `source` into `target`, each line
starting with its number:

```
1. Deauville Festival du Rire, first edition.
2. Four venues, four days, and a sea breeze between two shows.
```

`main()` prints the statistics of `data/review.txt`.

## shows_csv.py `[core]`

The festival team writes the programme in a spreadsheet and exports it as
[data/programme.csv](data/programme.csv). The program needs it in JSON.

| Function                         | Does                                                                        |
| -------------------------------- | --------------------------------------------------------------------------- |
| `load_csv(path)`                 | list of dicts, one per line; `duration` becomes an `int`, `price` a `float` |
| `save_json(shows, path)`         | writes the list, `indent=2`, `ensure_ascii=False`                           |
| `load_json(path)`                | reads it back                                                               |
| `save_csv(shows, path)` `[ext.]` | writes a CSV with the columns of `FIELDS`, in this order                    |

`main()` converts `data/programme.csv` into `programme.json` and prints
`10 shows written to programme.json`.
