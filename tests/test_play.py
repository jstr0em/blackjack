from src.blackjack import Blackjack
from src.cards import Deck
from src.participants import Dealer, Player

def test_play():
    player1 = Player("Jonathan", 400)
    dealer = Dealer()
    deck = Deck()
    blackjack = Blackjack([player1], dealer, deck)

    blackjack.play()