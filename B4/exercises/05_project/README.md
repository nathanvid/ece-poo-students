# 05 - The project becomes a package `[core]` - due before B5

Your `festival.py` of B3 holds everything in one file. The project now takes
its final shape: a package that you design, with the tools of this block
(encapsulation, inheritance, abstract classes, modules).

## Get the starter

The trainer gives the link of the template repository `deauville-starter`.
It holds no code: the brief, the data, the website and the admin, and the
API contract. Keep your own repository and its history:

1. On the template page: **Code → Download ZIP**, unzip it.
2. Copy its content into your repository folder (with the hidden file
   `.gitignore`).
3. Move your B3 `festival.py`, `test_festival.py` and `programme.json` into
   a folder `b3/`: you will reuse ideas and code from them.
4. Read the brief, `README.md`, entirely. Commit:
   `Add the project brief, data and website`.

## Design before you code

The brief gives the rules, not the classes. On paper, or in a `DESIGN.md`:

- the classes, what each one holds and which rules it checks;
- the family of performances: what is common, what each kind adds;
- your errors: how a caller knows _which_ rule was broken;
- the modules: one subject per file, and who imports whom;
- how storage stays apart from the model.

Show it to the trainer or to another student before writing the code. Then:

```bash
uv init --package --name <your-package-name>
uv add --dev pytest ruff
```

The B3 version shows what must change: public lists anyone can `append` to,
`ValueError` for every problem, a single kind of show, a day compared as a
string. The exercises of this block are small versions of the answers.

## Order of work

One class at a time, each with its tests in `tests/`: write a test of a rule,
see it fail, make it pass, commit. Suggested order: names and slugs, artist
and venue, performances, the festival and its rules, loading and saving, the
command line.

An AI assistant can help, but it does not take the decisions of the section
above for you: at the oral you explain your structure and change it live.

## Due before B5

- your design in the README (or `DESIGN.md`);
- the rules of the brief hold, each with at least one test;
- loading and saving `data/festival.json`;
- a command line that shows the programme of `2027-06-11`, night included;
- `uv run pytest` and `uv run ruff check .` pass.

The web server is the subject of B5.
