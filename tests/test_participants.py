from blackjack.participants import Dealer, Player
from blackjack.cards import Cards, Deck

# Tests that we can add a player and place some initial bets.
def test_player():
    # Creates a player called Jack that has a 1000 credits
    player = Player("Jack", 1000)
    assert player.name == "Jack"
    assert player.credit == 1000
    assert isinstance(player.cards, Cards)

    # Jack places a 200 credit bet
    player.place_bet(200)
    assert player.bet == 200
    assert player.credit == 800


def test_dealer():
    # Creates a dealer
    dealer = Dealer()
    assert isinstance(dealer.cards, Cards)

    # Creates a deck
    deck = Deck()
    assert len(deck) == 52