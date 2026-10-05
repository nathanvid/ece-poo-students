# Example 04 - input() in a script
# Run: uv run python B1/examples/04_input_output.py
#
# input() waits for Enter and always returns a str.

name = input("Your name: ")
print(f"Hello {name}!")

age = int(input("Your age: "))
print(f"Next year you will be {age + 1}.")

first = input("First number: ")
second = input("Second number: ")
print("Without conversion:", first + second)
print("With conversion:", int(first) + int(second))

height = float(input("Your height in metres: "))
print(f"That is {height * 100:.0f} cm.")

# Ask again while the answer is not valid.
seats = int(input("How many seats in the venue? "))
while seats <= 0:
    print("A venue needs at least one seat.")
    seats = int(input("How many seats in the venue? "))
print(f"OK, {seats} seats.")

ticket_count = int(input("How many tickets? "))
unit_price = 22.0
total = ticket_count * unit_price
print(f"{ticket_count} ticket(s) x {unit_price:.2f} EUR = {total:.2f} EUR")

answer = input("Programme booklet? (y/n) ").strip().lower()
print(f"Answer received: {answer!r}")
