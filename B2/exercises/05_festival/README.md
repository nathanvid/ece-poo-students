# 05 - Festival, first version `[core]` - due before B3

Check: `uv run pytest B2 -k festival`

The programme now lives in [programme.json](programme.json) (the 10 shows of
B1). `festival.py` loads it, shows the programme of a day, adds a show if the
rules allow it, and saves the file.

```
10 shows loaded.
Command (day/add/quit): day
Day (YYYY-MM-DD): 2027-06-11
Programme for 2027-06-11:
15:00-17:00 | Le Kiosque | Improv Lab (Inès Moreau)
18:00-19:10 | Théâtre des Planches | Family Business (Sacha Diallo)
20:30-21:50 | Grand Casino | Tall Tales (Léa Fontaine)
23:30-00:30 | Le Kiosque | Late Laughs (Nora Lebrun)
Command (day/add/quit): add
Title: Too Soon
Artist: Max Pellerin
Venue: Grand Casino
Day: 2027-06-10
Start (HH:MM): 22:45
Duration (min): 60
Price (EUR): 10
Error: Grand Casino is busy with Opening Gala (20:30-22:30).
Command (day/add/quit): quit
```

`main()`, `ask_show()` and `print_day()` are written. Write the other
functions; their docstrings say what they do. Several of them are close to
what you wrote in `timing.py` and `check_show.py`: copy and adapt.

## The rules

- A venue needs **30 minutes** between the end of a show and the start of the
  next one (`VENUE_CHANGEOVER`).
- An artist needs **30 minutes** between two shows (`ARTIST_REST`).
- Only shows of the same day are compared.

`find_clash(shows, new_show)` returns the message of the first conflict found,
checking the venue before the artist for each show:

```
Grand Casino is busy with Opening Gala (20:30-22:30).
Nora Lebrun is already on stage in Late Laughs (23:30-00:30).
```

and `None` if the new show fits. `add_show` checks the show, then the
conflicts, and raises a `ValueError` with the message; nothing is added.

`shows_of_day` sorts with `sorted(..., key=start_of)`.

## Your project repository

When the tests pass, the project leaves the course folder: follow
[git.md](../../git.md) to create the repository `deauville-festival` on
GitHub, with:

```
deauville-festival/
├── .gitignore
├── README.md          # what the program does, how to run it
├── festival.py
└── programme.json
```

Commit, push, and send the link of the repository. From now on the project
is only in this repository.
