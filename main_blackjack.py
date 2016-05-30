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
        self.players_bank = 100
        print("-" * 40)
        print("Player starts with ${}. Game ends when bank empty. $10 per hand.".format(self.players_bank))
        self.game = PlayTheHands()
        self.launch_game()
        self.play_out_the_bank()

    def launch_game(self):
        self.game.opening()
        self.game.players_logic()
        self.game.dealers_logic()

    def play_out_the_bank(self):
        while self.players_bank > 0:
            print("=" * 40)
            self.players_bank += self.game.bet
            if self.players_bank > 0:
                print("Player's bank at ${}.".format(self.players_bank))
                self.game.__init__()
                self.game.opening()
                self.game.players_logic()
                self.game.dealers_logic()
        print("Player's bank is empty. Game over.")


fabulous_blackjack = BlackJack()
