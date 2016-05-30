# launches game
# announces winner
# invites to play again
# bonus: add $100 bank

# from hand import Hand
# from deck import Deck
from player import PlayTheHands
import sys


class BlackJack:

    def __init__(self):
        print("-" * 40)
        print("Time to play some blackjack. \nHere's how the game opens: \n")
        self.game = PlayTheHands()
        self.launch_game()
        self.play_again()

    def launch_game(self):
        self.game.opening()
        self.game.players_logic()
        self.game.dealers_logic()

    def winner(self):
        pass

    def play_again(self):
        print("=" * 40)
        while True:
            play_on = input("Want to play another hand? Y/n ").lower()
            if play_on == 'y':
                return
                # self.launch_game()
            else:
                sys.exit()

fabulous_blackjack = BlackJack()
