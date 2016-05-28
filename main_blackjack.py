from hand import Hand
import sys


class PlayTheGame():

    def __init__(self):
        print("Time to play some blackjack.")
        self.launch_game()
        self.play_again()

    @staticmethod
    def launch_game():
        new_round = Hand()
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

