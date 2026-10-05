"""A first web API: greetings and a small calculator.

Start it, then open http://127.0.0.1:8000/docs:

    uv run python B5/exercises/01_first_routes/hello_api.py
"""

from fastapi import FastAPI

GREETINGS = {"en": "Hello", "fr": "Bonjour", "es": "Hola"}

app = FastAPI(title="Hello")


@app.get("/")
def home() -> dict:
    return {"message": "Welcome to the Deauville Festival du Rire."}


# Write the routes /hello/{name}, /add and /languages here.


def main() -> None:
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
