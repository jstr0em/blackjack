from blackjack.blackjack import Blackjack
from blackjack.cards import Deck
from blackjack.participants import Dealer, Player

def test_play():
    player1 = Player("Jonathan", 400)
    dealer = Dealer()
    deck = Deck()
    blackjack = Blackjack([player1], dealer, deck)

    blackjack.play()