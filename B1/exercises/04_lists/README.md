# 04 - Lists

Check: `uv run pytest B1 -k lists`

## grades.py `[core]`

Ask grades (decimal numbers) until the user presses Enter without typing
anything. Store them in a list, then print the statistics below. Grades above
the average are listed in the order they were typed, separated by `,` .

```
Grade (empty to stop): 12
Grade (empty to stop): 8
Grade (empty to stop): 17.5
Grade (empty to stop): 13.5
Grade (empty to stop):
Count: 4
Lowest: 8.0
Highest: 17.5
Average: 12.75
Above average: 17.5, 13.5
```

With no grade at all, print `No grades.` If no grade is above the average
(all grades equal), print `Above average: none`.

## words.py `[core]`

Ask a sentence and print the number of words, the words in reverse order, and
the longest word (the first one if there is a tie). An empty sentence prints
`No words.`

```
Sentence: the show must go on
Words: 5
Reversed: on go must show the
Longest: show
```

Build the reversed list yourself with a loop (no `reverse()`, no `[::-1]`).

## running_order.py `[core]`

The host of a lineup prepares the running order with a small menu.
Repeat `Command (add/remove/show/quit):`  (upper case and spaces around the
command are accepted).


| Command       | Behaviour                                                                                                                                                                                                                                           |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `add`         | Already 6 acts: `The lineup is full.` and nothing else is asked. Otherwise ask `Name:` . Empty name: `Name cannot be empty.` Already there: `Nora Lebrun is already in the lineup.` Otherwise add it at the end: `Nora Lebrun added in position 1.` |
| `remove`      | Ask `Name:` . Present: `Nora Lebrun removed.` Absent: `Nora Lebrun is not in the lineup.`                                                                                                                                                           |
| `show`        | The numbered list (`1. Nora Lebrun`), or `The lineup is empty.`                                                                                                                                                                                     |
| `quit`        | Leave the menu.                                                                                                                                                                                                                                     |
| anything else | `Unknown command: dance`                                                                                                                                                                                                                            |


After `quit`, print `Final lineup: 2 act(s).` and the numbered list.

```
Command (add/remove/show/quit): add
Name: Nora Lebrun
Nora Lebrun added in position 1.
Command (add/remove/show/quit): add
Name: Max Pellerin
Max Pellerin added in position 2.
Command (add/remove/show/quit): add
Name: Nora Lebrun
Nora Lebrun is already in the lineup.
Command (add/remove/show/quit): dance
Unknown command: dance
Command (add/remove/show/quit): quit
Final lineup: 2 act(s).
1. Nora Lebrun
2. Max Pellerin
```



## seat_map.py `[ext.]`

Le Kiosque has 5 rows of 8 seats. Store the hall as a list of 5 rows, each row
being a list of 8 strings: `"."` for free, `"X"` for booked.

Repeat `Seat (row seat), empty to stop:` . The user types a row and a seat,
counted from 1, e.g. `2 5`.


| Answer                        | Output                     |
| ----------------------------- | -------------------------- |
| empty                         | stop asking                |
| not exactly two whole numbers | `Please type two numbers.` |
| outside the hall              | `No such seat.`            |
| already booked                | `Seat already taken.`      |
| otherwise                     | `Seat 2-5 booked.`         |


Then print the map and the number of free seats:

```
STAGE
Row 1: . . . . . . . .
Row 2: . . . . X . . .
Row 3: . . . . . . . .
Row 4: . . . . . . . .
Row 5: . . . . . . . .
Seats left: 39
```

Hints: `"2 5".split()` gives `["2", "5"]`, `"12".isdigit()` gives `True`,
`hall[1][4]` is row 2 seat 5.