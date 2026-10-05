# 05 - Dictionaries

Check: `uv run pytest B1 -k dicts`

## word_count.py `[core]`

Ask a sentence and count how many times each word appears, ignoring upper and
lower case. Print the words in the order they first appear. An empty sentence
prints `No words.`

```
Sentence: Ha ha HA hi ha
ha: 4
hi: 1
```

## phone_book.py `[core]`

`CONTACTS` is already written in the file. Ask names until the user presses
Enter without typing anything, and print the number of each one. At the end,
print how many contacts the book holds.

```
Name (empty to stop): Alice
Alice: 01 23 45 67 89
Name (empty to stop): Zoé
Unknown contact: Zoé
Name (empty to stop):
3 contacts in the book.
```

## programme.py `[core]` - due before B2

`PROGRAMME` holds the 10 shows of the festival, in chronological order. Each
show is a dict:

```python
{
    "title": "Opening Gala",
    "artist": "Paul Kerbrat",
    "venue": "Grand Casino",
    "day": "2027-06-10",
    "start": "20:30",
    "duration": 120,  # minutes
    "price": 35.0,  # EUR
}
```

Do not change the data. The program prints five parts, in this order.

**1. Programme of one day.** Ask `Day (YYYY-MM-DD): `, print
`Programme for 2027-06-10:` then one line per show of that day:

```
20:30 | Grand Casino | Opening Gala (Paul Kerbrat, 120 min)
```

No show that day: `No show that day.`

**2. Shows per venue**, venues in order of first appearance:

```
Shows per venue:
- Grand Casino: 4
- Théâtre des Planches: 3
- Le Kiosque: 3
```

**3. Longest show** (the first one if there is a tie):

```
Longest show: Closing Gala (130 min)
```

**4. Artists with several shows**, in order of first appearance:

```
Artists with several shows:
- Paul Kerbrat (2 shows)
- ...
```

**5. Average ticket price** (free shows count as 0):

```
Average ticket price: 19.30 EUR
```

Constraints:

- no `max(..., key=...)`, no `sorted(..., key=...)`, no `collections.Counter`;
- nothing from the data written in your code (no `4`, no `"Closing Gala"`):
  the tests add a show to `PROGRAMME` and check that your results follow.
