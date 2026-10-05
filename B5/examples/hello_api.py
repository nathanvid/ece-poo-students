"""A web API in a few lines. Start it:

    uv run python B5/examples/hello_api.py

then open http://127.0.0.1:8000/docs in a browser. Ctrl+C stops the server.
"""

import uvicorn
from fastapi import FastAPI, HTTPException

VENUES = [
    {"slug": "grand-casino", "name": "Grand Casino", "capacity": 650},
    {"slug": "le-kiosque", "name": "Le Kiosque", "capacity": 120},
]

app = FastAPI(title="Hello festival")


@app.get("/")
def home() -> dict:
    return {"message": "Welcome to the Deauville Festival du Rire."}


@app.get("/venues")
def list_venues(min_capacity: int = 0) -> list[dict]:
    result = []
    for venue in VENUES:
        if venue["capacity"] >= min_capacity:
            result.append(venue)
    return result


@app.get("/venues/{slug}")
def read_venue(slug: str) -> dict:
    for venue in VENUES:
        if venue["slug"] == slug:
            return venue
    raise HTTPException(status_code=404, detail=f"Unknown venue: {slug}.")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
