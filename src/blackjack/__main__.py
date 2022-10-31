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


def welcome():
    print("Welcome to Blackjack!")


def show_choices():
    print("1) Play game")
    print("2) Quick match")
    print("3) Options")
    print("4) Exit")


def play_game():
    pass


def quick_match():
    pass


def options():
    pass


def main():
    welcome()

    while True:
        show_choices()

        try:
            choice = int(input("Enter a number: "))
        except ValueError:
            print("Invalid input.")
            continue

        if choice < 1 or choice > 4:
            print("Pick a valid choice.")
        else:
            break
    
        if choice == 1:
            play_game()
        elif choice == 2:
            quick_match()
        elif choice == 3:
            options
        elif choice == 4:
            pass


if __name__ == "__main__":
    main()