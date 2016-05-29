from hand import Hand
from deck import Deck
from player import Player
import sys


class PlayTheGame:

    def __init__(self):
        print("Time to play some blackjack.")
        # self.launch_game()
        # self.play_again()
        self.deck = Deck()
        self.new_round = Hand()

    # should i turn these into self.new_round?
    def launch_game(self):
        self.deck.initial_deal()
        self.new_round.players_hand()
        self.new_round.dealers_hand()

    def play_again(self):
        while True:
            play_on = input("Want to play another hand? Y/n ").lower()
            if play_on == 'y':
                self.launch_game()
            else:
                sys.exit()

fabulous_blackjack = PlayTheGame()

