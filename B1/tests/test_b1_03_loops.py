import pytest

from checks import assert_in_order, lines


def test_countdown(run_script):
    output = run_script("03_loops/countdown.py", lines("3"))
    assert output.split("Start: ")[1].split() == ["3", "2", "1", "Go!"]


@pytest.mark.parametrize("start", ["0", "-5"])
def test_countdown_invalid(run_script, start):
    output = run_script("03_loops/countdown.py", lines(start))
    assert "Start must be at least 1." in output
    assert "Go!" not in output


def test_times_table(run_script):
    output = run_script("03_loops/times_table.py", lines("7"))
    expected = [f"7 x {i} = {7 * i}" for i in range(1, 11)]
    assert_in_order(output, *expected)
    assert "7 x 11" not in output and "7 x 0" not in output


def test_running_total(run_script):
    output = run_script("03_loops/running_total.py", lines("4", "10", "-2", "0"))
    assert_in_order(output, "Count: 3", "Sum: 12", "Average: 4.00")


def test_running_total_empty(run_script):
    output = run_script("03_loops/running_total.py", lines("0"))
    assert "No numbers." in output
    assert "Count" not in output


def test_lineup_duration_example(run_script):
    output = run_script(
        "03_loops/lineup_duration.py", lines("20:30", "3", "20", "-5", "30", "39")
    )
    assert output.count("Invalid duration, try again.") == 1
    assert_in_order(output, "Total duration: 1h35", "Ends at: 22:05")


@pytest.mark.parametrize(
    ("answers", "total", "end"),
    [
        (("21:00", "1", "45"), "0h45", "21:45"),  # one act: no break
        (("18:00", "2", "60", "59"), "2h02", "20:02"),  # minutes on 2 digits
        (("23:30", "2", "45", "42"), "1h30", "01:00"),  # after midnight
        (("09:05", "1", "5"), "0h05", "09:10"),  # hours on 2 digits
    ],
)
def test_lineup_duration(run_script, answers, total, end):
    output = run_script("03_loops/lineup_duration.py", lines(*answers))
    assert_in_order(output, f"Total duration: {total}", f"Ends at: {end}")


def test_lineup_duration_zero_is_invalid(run_script):
    output = run_script(
        "03_loops/lineup_duration.py", lines("20:00", "1", "0", "0", "10")
    )
    assert output.count("Invalid duration, try again.") == 2
    assert "Total duration: 0h10" in output


@pytest.mark.parametrize("count", ["0", "-2"])
def test_lineup_duration_needs_one_act(run_script, count):
    output = run_script("03_loops/lineup_duration.py", lines("20:00", count))
    assert "A lineup needs at least one act." in output
    assert "Total duration" not in output
