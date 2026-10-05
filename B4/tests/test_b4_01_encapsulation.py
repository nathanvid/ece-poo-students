import pytest


@pytest.fixture
def wallet(load_exercise):
    return load_exercise("01_encapsulation/wallet.py")


@pytest.fixture
def lineup(load_exercise):
    return load_exercise("01_encapsulation/lineup.py")


# --- wallet ------------------------------------------------------------------------


def test_wallet(wallet):
    lina = wallet.Wallet("Lina")
    assert lina.owner == "Lina"
    assert lina.balance == 0.0
    lina.top_up(20)
    lina.pay(4.5)
    assert lina.balance == 15.5
    assert lina.history() == [20, -4.5]


def test_wallet_balance_is_read_only(wallet):
    lina = wallet.Wallet("Lina")
    with pytest.raises(AttributeError):
        lina.balance = 1000
    assert "_balance" in vars(lina), "Keep the balance in self._balance."


def test_wallet_refuses_wrong_amounts(wallet):
    lina = wallet.Wallet("Lina")
    with pytest.raises(ValueError, match="Invalid amount: 0."):
        lina.top_up(0)
    lina.top_up(10)
    with pytest.raises(ValueError, match="Invalid amount: -5."):
        lina.pay(-5)
    with pytest.raises(ValueError, match="Balance too low: 10.00 EUR."):
        lina.pay(12)
    assert lina.balance == 10
    assert lina.history() == [10]


def test_wallet_history_is_a_copy(wallet):
    lina = wallet.Wallet("Lina")
    lina.top_up(10)
    lina.history().append(1000)
    assert lina.history() == [10]


# --- lineup ------------------------------------------------------------------------


def make_gala(lineup):
    gala = lineup.Lineup("Opening Gala", "Paul Kerbrat")
    for name in ["Nora Lebrun", "Max Pellerin", "Léa Fontaine"]:
        gala.add_act(name)
    return gala


def test_lineup(lineup):
    gala = make_gala(lineup)
    assert gala.title == "Opening Gala"
    assert gala.host == "Paul Kerbrat"
    assert gala.acts == ["Nora Lebrun", "Max Pellerin", "Léa Fontaine"]
    assert len(gala) == 3
    assert str(gala) == (
        "Opening Gala, hosted by Paul Kerbrat: Nora Lebrun, Max Pellerin, Léa Fontaine"
    )


def test_lineup_is_protected(lineup):
    gala = make_gala(lineup)
    gala.acts.append("Sneaky")
    assert len(gala) == 3
    with pytest.raises(AttributeError):
        gala.host = "Somebody"
    with pytest.raises(AttributeError):
        gala.acts = []


def test_add_act_rules(lineup):
    gala = make_gala(lineup)
    gala.add_act("  Sacha Diallo ")
    assert gala.acts[-1] == "Sacha Diallo"
    with pytest.raises(ValueError, match="An act needs a name."):
        gala.add_act("  ")
    with pytest.raises(ValueError, match="paul kerbrat is the host."):
        gala.add_act("paul kerbrat")
    with pytest.raises(ValueError, match="NORA LEBRUN is already in the lineup."):
        gala.add_act("NORA LEBRUN")
    gala.add_act("Karim Benali")
    gala.add_act("Inès Moreau")
    with pytest.raises(ValueError, match=r"The lineup is full \(6 acts\)."):
        gala.add_act("Tom Vasseur")
    assert lineup.MAX_ACTS == 6


def test_remove_and_move_up(lineup):
    gala = make_gala(lineup)
    gala.move_up("léa fontaine")
    assert gala.acts == ["Nora Lebrun", "Léa Fontaine", "Max Pellerin"]
    gala.move_up("Nora Lebrun")
    assert gala.acts[0] == "Nora Lebrun"
    gala.remove_act("max pellerin")
    assert gala.acts == ["Nora Lebrun", "Léa Fontaine"]
    with pytest.raises(ValueError, match="Max Pellerin is not in the lineup."):
        gala.remove_act("Max Pellerin")
    with pytest.raises(ValueError, match="is not in the lineup"):
        gala.move_up("Nobody")
