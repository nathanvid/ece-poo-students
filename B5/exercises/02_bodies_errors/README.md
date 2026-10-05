# 02 - Bodies and errors

Check: `uv run pytest B5 -k bodies_errors`

```bash
uv run python B5/exercises/02_bodies_errors/venues_api.py
```

## venues_api.py `[core]`

`Venue`, `VenueIn` and `BookingIn` are given. `Venue` checks its own data and
raises a `ValueError`; the routes do not check anything a second time.

Everything else goes in `create_app()`, which builds a new application with
its own `venues` dict (key: the slug). Write `find_venue`, the two exception
handlers, then the routes.

| Request                 | Success                                        | Errors                                                |
| ----------------------- | ---------------------------------------------- | ----------------------------------------------------- |
| `GET /venues`           | `200`, list of `to_dict()`, in the order added |                                                       |
| `GET /venues/{slug}`    | `200`, the venue                               | `404` `Unknown venue: nowhere.`                       |
| `POST /venues`          | `201`, the new venue                           | `409` `Le Kiosque already exists.` (same slug), `422` |
| `DELETE /venues/{slug}` | `204`, no body                                 | `404`                                                 |

The body of `POST /venues`:

```json
{ "name": "Le Kiosque", "capacity": 120, "address": "Beach promenade" }
```

A capacity of 0 or an empty name: `Venue` raises a `ValueError`, the handler
answers `422` with `{"detail": "A venue needs at least one seat, got 0."}`.
The 409 message uses the name of the venue already there.

## Bookings `[ext.]`

`POST /venues/{slug}/bookings` with `{"seats": 8}` calls `venue.book(8)` and
answers `201` with the venue (`seats_left` has changed).
`NotEnoughSeatsError` becomes a `409` (`Not enough seats: 2 left.`), with a
second handler.
