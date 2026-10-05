from checks import assert_in_order, lines, run_python


def test_word_count(run_script):
    output = run_script("05_dicts/word_count.py", lines("Ha ha HA hi ha"))
    assert_in_order(output, "ha: 4", "hi: 1")


def test_word_count_order_of_appearance(run_script):
    output = run_script("05_dicts/word_count.py", lines("to be or not to be"))
    assert_in_order(output, "to: 2", "be: 2", "or: 1", "not: 1")


def test_word_count_empty(run_script):
    assert "No words." in run_script("05_dicts/word_count.py", lines(""))


def test_phone_book(run_script):
    output = run_script("05_dicts/phone_book.py", lines("Alice", "Zoé", "  Chloé ", ""))
    assert_in_order(
        output,
        "Alice: 01 23 45 67 89",
        "Unknown contact: Zoé",
        "Chloé: 07 98 76 54 32",
        "3 contacts in the book.",
    )


def test_programme_day_listing(run_script):
    output = run_script("05_dicts/programme.py", lines("2027-06-10"))
    assert_in_order(
        output,
        "Programme for 2027-06-10:",
        "20:30 | Grand Casino | Opening Gala (Paul Kerbrat, 120 min)",
        "21:00 | Théâtre des Planches | Nothing Serious (Nora Lebrun, 75 min)",
        "22:30 | Le Kiosque | Open Mic Night (Max Pellerin, 90 min)",
        "Shows per venue:",
    )
    assert "No show that day." not in output
    assert "Improv Lab" not in output


def test_programme_day_without_show(run_script):
    output = run_script("05_dicts/programme.py", lines("2027-06-13"))
    assert_in_order(output, "Programme for 2027-06-13:", "No show that day.")


def test_programme_statistics(run_script):
    output = run_script("05_dicts/programme.py", lines("2027-06-13"))
    assert_in_order(
        output,
        "Shows per venue:",
        "- Grand Casino: 4",
        "- Théâtre des Planches: 3",
        "- Le Kiosque: 3",
        "Longest show: Closing Gala (130 min)",
        "Artists with several shows:",
        "- Paul Kerbrat (2 shows)",
        "- Nora Lebrun (2 shows)",
        "- Sacha Diallo (2 shows)",
        "Average ticket price: 19.30 EUR",
    )
    assert "Karim Benali (" not in output


def test_programme_follows_the_data(code_dir, tmp_path):
    source = (code_dir / "05_dicts/programme.py").read_text(encoding="utf-8")
    marker = "\n# --- 1."
    assert marker in source, "Keep the '# --- 1.' comment in programme.py."
    extra_show = (
        "PROGRAMME.append({'title': 'Midnight Marathon', 'artist': 'Karim Benali',"
        " 'venue': 'Le Phare', 'day': '2027-06-13', 'start': '23:00',"
        " 'duration': 240, 'price': 5.0})\n"
    )
    modified = tmp_path / "programme.py"
    modified.write_text(
        source.replace(marker, "\n" + extra_show + marker, 1), encoding="utf-8"
    )

    result = run_python(modified, lines("2027-06-13"))
    assert result.returncode == 0, result.stderr
    assert_in_order(
        result.stdout,
        "23:00 | Le Phare | Midnight Marathon (Karim Benali, 240 min)",
        "- Le Phare: 1",
        "Longest show: Midnight Marathon (240 min)",
        "- Karim Benali (2 shows)",
        "Average ticket price: 18.00 EUR",
    )
