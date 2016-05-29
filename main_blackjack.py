# creates player's hand
# creates dealer's hand
# plays out player's hand
# plays out dealer's hand

from hand import Hand
from deck import Deck
import sys


class BlackJack:

    def __init__(self):
        print("Time to play some blackjack.")
        # self.launch_game()
        # self.play_again()


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

