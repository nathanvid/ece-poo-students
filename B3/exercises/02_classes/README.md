# 02 - Writing classes

Check: `uv run pytest B3 -k classes`

Write the body of each method: `__init__` first.

## rectangle.py `[core]`

`Rectangle(width, height)` stores `width` and `height`. Methods: `area()`,
`perimeter()`, `is_square()`, and `scale(factor)` which multiplies both sides
(it changes the rectangle and returns nothing).

## counter.py `[core]`

`Counter(name)` stores `name` and a `value` starting at 0. Methods:
`increment(step=1)` and `reset()`.

The class attribute `created` counts the counters made so far: each new
counter adds 1 to it. It belongs to the class, not to each counter.

## venue.py `[core]`

`Venue(name, capacity)` stores `name`, `capacity` and `sold` (0 at the
start). A capacity below 1 raises
`ValueError("A venue needs at least one seat, got 0.")`.

| Method          | Does                                                 |
| --------------- | ---------------------------------------------------- |
| `seats_left()`  | seats not sold                                       |
| `is_full()`     | no seat left                                         |
| `occupancy()`   | percentage sold: `75.0` for 90 seats sold out of 120 |
| `book(count)`   | sells `count` seats                                  |
| `cancel(count)` | gives back `count` seats                             |

`book` raises a `ValueError`:

- `A booking is 1 to 10 seats, got 11.` outside 1 to `MAX_PER_BOOKING`;
- `Not enough seats: 2 left.` when there are not enough seats.

`cancel` raises `ValueError("Only 12 seats sold.")` when giving back more
than sold. After an error, nothing has changed.

`MAX_PER_BOOKING` is a class attribute: the same limit for every venue.
