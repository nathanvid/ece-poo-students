"""The jokes of the festival, read through a web API.

uv run python B5/exercises/01_first_routes/jokes_api.py
"""

from fastapi import FastAPI, HTTPException

JOKES = [
    {
        "id": 1,
        "artist": "Nora Lebrun",
        "text": "I told my plants a joke. Nothing grew.",
        "likes": 12,
    },
    {
        "id": 2,
        "artist": "Max Pellerin",
        "text": "My GPS has an accent. I am lost, but charmed.",
        "likes": 30,
    },
    {
        "id": 3,
        "artist": "Nora Lebrun",
        "text": "My alarm clock and I are not on speaking terms.",
        "likes": 7,
    },
    {
        "id": 4,
        "artist": "Sacha Diallo",
        "text": "I tried to be normal once. Worst two minutes of my life.",
        "likes": 25,
    },
    {
        "id": 5,
        "artist": "Inès Moreau",
        "text": "Improv is like cooking without a recipe, for strangers.",
        "likes": 18,
    },
]

app = FastAPI(title="Jokes")


def find_joke(joke_id: int) -> dict:
    """The joke with this id. Raises HTTPException (404) if there is none."""
    raise NotImplementedError


@app.get("/jokes")
def list_jokes(artist: str | None = None, limit: int = 10) -> list[dict]:
    """Jokes in id order; `artist` keeps one artist (any case), `limit` cuts."""
    raise NotImplementedError


# Write the routes /jokes/top, /jokes/{joke_id} and /stats here.
# Careful with the order: /jokes/top must come before /jokes/{joke_id}.


def main() -> None:
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
