from hand import Hand
from deck import Deck
from player import Player
import sys


class PlayTheGame:

    def __init__(self):
        print("Time to play some blackjack.")
        self.launch_game()
        self.play_again()

    # @staticmethod >>> pycharm suggests this. i don't understand the benefit, so didn't implement.
    def launch_game(self):
        new_round = Hand()
        # deck = Deck()  # added this
        new_round.players_hand()
        new_round.dealers_hand()

    def play_again(self):
        while True:
            play_on = input("Want to play another hand? Y/n ").lower()
            if play_on == 'y':
                self.launch_game()
            else:
                sys.exit()

fabulous_blackjack = PlayTheGame()

