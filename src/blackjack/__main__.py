import imp
import sys
from blackjack.participants import Player, Dealer
from blackjack.blackjack import Blackjack
from blackjack.cards import Deck

def generate_players(player_name_credit_list):
    players = []
    for i in range(0, len(player_name_credit_list), 2):
        name = player_name_credit_list[i]
        credit = player_name_credit_list[i+1]
        player = Player(name, credit)
        players.append(player)

    return players
        
def main():
    players = generate_players(sys.argv[1:])
    dealer = Dealer()
    deck = Deck()
    
    blackjack = Blackjack(players, dealer, deck)
    blackjack.play_round()

if __name__ == "__main__":
    main()