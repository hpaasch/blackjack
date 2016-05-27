from hand import Hand
import sys


#class PlayTheGame():

def launch_game():
    new_round = Hand()
    new_round.players_hand()
    new_round.dealers_hand()
    # new_round.play_again()

# '''


def play_again():
    play_on = input("Want to play another hand? Y/n ").lower()
    while True:  # this needs a WHILE loop or it only replays once
        if play_on == 'y':
            launch_game()
        else:
            sys.exit()
    # '''

launch_game()
play_again()
