# creates player's hand
# creates dealer's hand
# plays out player's hand
# plays out dealer's hand

from hand import Hand
from deck import Deck
import sys


class PlayTheGame:
    def __init__(self):
        print("Time to play some blackjack.")
        self.deck = Deck()
        self.players_hand = Hand()
        self.dealers_hand = Hand()

    def players_logic(self):
        while self.players_hand.value_the_cards() < 21:
            hit = input("Hit or Stay? H/S ").lower()
            if hit == 'h':
                Hand.draw_a_card(self.players_hand)
                new_value = Hand.value_the_cards(self.players_hand)
                print("Player's cards tally: ", self.players_hand.value_the_cards())
                if self.players_hand.value_the_cards() > 21:
                    print("Player's hand is a bust.")
            else:
                print("Player's cards tally: ", self.players_hand.value_the_cards())
                break
        player_total = self.player_one.hand_total
        return player_total


fabulous_blackjack = PlayTheGame()

