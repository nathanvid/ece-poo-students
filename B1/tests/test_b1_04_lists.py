from checks import assert_in_order, lines


def test_grades(run_script):
    output = run_script("04_lists/grades.py", lines("12", "8", "17.5", "13.5", ""))
    assert_in_order(
        output,
        "Count: 4",
        "Lowest: 8.0",
        "Highest: 17.5",
        "Average: 12.75",
        "Above average: 17.5, 13.5",
    )


def test_grades_all_equal(run_script):
    output = run_script("04_lists/grades.py", lines("10", "10", ""))
    assert_in_order(output, "Count: 2", "Average: 10.00", "Above average: none")


def test_grades_empty(run_script):
    output = run_script("04_lists/grades.py", lines(""))
    assert "No grades." in output
    assert "Count" not in output


def test_words(run_script):
    output = run_script("04_lists/words.py", lines("the show must go on"))
    assert_in_order(
        output, "Words: 5", "Reversed: on go must show the", "Longest: show"
    )


def test_words_extra_spaces_and_tie(run_script):
    output = run_script("04_lists/words.py", lines("  big   cat  ran "))
    assert_in_order(output, "Words: 3", "Reversed: ran cat big", "Longest: big")


def test_words_empty(run_script):
    assert "No words." in run_script("04_lists/words.py", lines("   "))


def test_running_order_example(run_script):
    output = run_script(
        "04_lists/running_order.py",
        lines(
            "add", "Nora Lebrun",
            "add", "Max Pellerin",
            "add", "Nora Lebrun",
            "dance",
            "quit",
        ),
    )  # fmt: skip
    assert_in_order(
        output,
        "Nora Lebrun added in position 1.",
        "Max Pellerin added in position 2.",
        "Nora Lebrun is already in the lineup.",
        "Unknown command: dance",
        "Final lineup: 2 act(s).",
        "1. Nora Lebrun",
        "2. Max Pellerin",
    )


def test_running_order_remove_and_show(run_script):
    output = run_script(
        "04_lists/running_order.py",
        lines(
            "show",
            "add", "Nora Lebrun",
            "add", "Max Pellerin",
            "remove", "Nora Lebrun",
            "remove", "Nobody",
            "show",
            "quit",
        ),
    )  # fmt: skip
    assert_in_order(
        output,
        "The lineup is empty.",
        "Nora Lebrun removed.",
        "Nobody is not in the lineup.",
        "1. Max Pellerin",
        "Final lineup: 1 act(s).",
        "1. Max Pellerin",
    )


def test_running_order_commands_are_cleaned(run_script):
    output = run_script(
        "04_lists/running_order.py", lines("  ADD ", "  Sacha Diallo  ", " QUIT")
    )
    assert "Sacha Diallo added in position 1." in output
    assert "Final lineup: 1 act(s)." in output


def test_running_order_empty_name(run_script):
    output = run_script("04_lists/running_order.py", lines("add", "   ", "quit"))
    assert "Name cannot be empty." in output
    assert "Final lineup: 0 act(s)." in output


def test_running_order_is_limited_to_six_acts(run_script):
    answers = []
    for number in range(1, 7):
        answers += ["add", f"Act {number}"]
    # The 7th "add" must not ask for a name: "quit" is read as the next command.
    answers += ["add", "quit"]
    output = run_script("04_lists/running_order.py", lines(*answers))
    assert "Act 6 added in position 6." in output
    assert "The lineup is full." in output
    assert "Final lineup: 6 act(s)." in output


def test_seat_map_bookings(run_script):
    output = run_script(
        "04_lists/seat_map.py",
        lines("2 5", "2 5", "1 1", "6 1", "3 0", "a b", "1", "5 8", ""),
    )
    assert_in_order(
        output,
        "Seat 2-5 booked.",
        "Seat already taken.",
        "Seat 1-1 booked.",
        "No such seat.",
        "No such seat.",
        "Please type two numbers.",
        "Please type two numbers.",
        "Seat 5-8 booked.",
        "STAGE",
        "Row 1: X . . . . . . .",
        "Row 2: . . . . X . . .",
        "Row 3: . . . . . . . .",
        "Row 4: . . . . . . . .",
        "Row 5: . . . . . . . X",
        "Seats left: 37",
    )


def test_seat_map_empty(run_script):
    output = run_script("04_lists/seat_map.py", lines(""))
    assert "Seats left: 40" in output
