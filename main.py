from cards import *
from participants import *

class Blackjack:
    symbol_values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}

    def __init__(self, players, dealer, deck):
        self.players = players
        self.dealer = dealer
        self.deck = deck

    def place_bets(self):
        for player in self.players:
            amount = float(input("%s, enter your bet: " % player.name))
            player.place_bet(amount)

    def value(self, player):
        value = 0
        
        for card in player.cards:
            if card.symbol != "Ace":
                value += Blackjack.symbol_values[card.symbol]
            elif card.symbol == "Ace":
                value += 11
                # TODO: Add more logic here
        return value

    def evaluate_scores(self, players, dealer):
        for player in players:
            self.evaluate_score(player, dealer)

    def evaluate_score(self, player, dealer):
        player_value = self.value(player)
        dealer_value = self.value(dealer)

        if player_value > 21:
            self.bust(player)
        elif player_value <= 21:
            if dealer_value > 21:
                self.bust(dealer)
            elif dealer_value == 21:
                if player_value == 21:
                    if len(dealer.cards) == 2 and len(player.cards) > 2:
                        self.bust(player)
                    elif len(player.cards) == 2 and len(dealer.cards) > 2:
                        self.win(player)
                    elif len(player.cards) == len(dealer.cards):
                        self.tie(player)
                elif player_value < 21:
                    self.bust(player)
            elif dealer_value < 21:
                if player_value > dealer_value:
                    self.win(player)
                elif player_value == dealer_value:
                    self.tie(player)
                elif player_value < dealer_value:
                    self.bust(player)


    def play(self):
        print("Welcome to Blackjack!")
        players = self.players
        dealer = self.dealer
        deck = self.deck

        #self.place_bets()
        dealer.deal_cards(players, deck)
        dealer.deal_card(dealer, deck)
        dealer.deal_cards(players, deck)
        self.evaluate_scores(players, dealer)

        #dealer.deal_card(dealer, deck, face_down = True)
        
        