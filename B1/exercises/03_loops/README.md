# 03 - Loops

Check: `uv run pytest B1 -k loops`

## countdown.py `[core]`

Ask a starting number, count down to 1, then print `Go!`. If the number is
below 1, print `Start must be at least 1.` instead.

```
Start: 3
3
2
1
Go!
```

## times_table.py `[core]`

Ask a number and print its multiplication table from 1 to 10.

```
Number: 7
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

## running_total.py `[core]`

Ask numbers until the user types `0`. Then print how many numbers were typed
(the final 0 does not count), their sum and their average with 2 decimals.
If the first number is 0, print `No numbers.`

```
Number (0 to stop): 4
Number (0 to stop): 10
Number (0 to stop): -2
Number (0 to stop): 0
Count: 3
Sum: 12
Average: 4.00
```

## lineup_duration.py `[core]`

A lineup is a show where several comedians follow one another on stage.
Between two acts, the host needs 3 minutes to introduce the next one.

1. Ask `Start time (HH:MM): ` (you may assume the format is right).
2. Ask `Number of acts: `. Below 1: print `A lineup needs at least one act.`
   and stop.
3. For each act, ask `Act 1 duration (min): `, `Act 2 duration (min): `...
   A duration of 0 or less prints `Invalid duration, try again.` and the same
   act is asked again.
4. Total = all the acts + 3 minutes between two consecutive acts.
5. Print the total as `Total duration: 1h35` (minutes on 2 digits) and the end
   time as `Ends at: 22:05`. After midnight, the clock starts again from 00:00.

```
Start time (HH:MM): 20:30
Number of acts: 3
Act 1 duration (min): 20
Act 2 duration (min): -5
Invalid duration, try again.
Act 2 duration (min): 30
Act 3 duration (min): 39
Total duration: 1h35
Ends at: 22:05
```

```
Start time (HH:MM): 23:30
Number of acts: 2
Act 1 duration (min): 45
Act 2 duration (min): 42
Total duration: 1h30
Ends at: 01:00
```

Hints:

- `"20:30".split(":")` gives `["20", "30"]`.
- Work in minutes since midnight, then convert back to hours and minutes.
