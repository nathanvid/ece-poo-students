# running_order.py - instructions in README.md

MAX_ACTS = 6

lineup = []

while True:
    command = input("Command (add/remove/show/quit): ").strip().lower()

    if command == "quit":
        break
