# creates player's hand
# creates dealer's hand
# plays out player's hand
# plays out dealer's hand

from hand import Hand
from deck import Deck
import sys


class PlayTheHands:
    def __init__(self):
        self.deck = Deck()
        self.players_hand = Hand()
        self.dealers_hand = Hand()
        self.bet = -10

    def opening(self):
        Hand.initial_deal(self.players_hand)
        Hand.initial_deal(self.dealers_hand)
        print("-" * 40)
        print("\nThe hand opens: \n")
        print("Dealer showing one: {}".format(self.dealers_hand.cards_in_hand[0]))
        print("Player showing: ", self.players_hand)
        print("Player's cards tally: ", self.players_hand.value_the_cards())

    def players_logic(self):
        print("-" * 40)
        while self.players_hand.value_the_cards() < 21:
            hit = input("Hit or Stay? H/S ").lower()
            if hit == 'h':
                Hand.draw_a_card(self.players_hand)
                print("Player holding: ", self.players_hand)
                print("Player's cards tally: ", self.players_hand.value_the_cards())
                if self.players_hand.value_the_cards() > 21:
                    print("Player's hand is a bust.")
            else:
                print("Player's cards tally: ", self.players_hand.value_the_cards())
                break
        return self.players_hand.value_the_cards()

    def dealers_logic(self):
        print("-" * 40)
        print("Dealer showing both now: ", self.dealers_hand)
        if self.players_hand.value_the_cards() > 21:
            # bank goes down by $10
            print("Dealer wins.")
            return self.dealers_hand.value_the_cards()
        while self.dealers_hand.value_the_cards() < 17:
            Hand.draw_a_card(self.dealers_hand)
            print("Dealer takes a card: ", self.dealers_hand)
        if self.dealers_hand.value_the_cards() > 21:
            print("Dealer's hand busted at {}. Player wins.".format(self.dealers_hand.value_the_cards()))
        elif self.dealers_hand.value_the_cards() == self.players_hand.value_the_cards():
            print("Dealer: {}. Player: {}. Dealer wins ties.".format(self.dealers_hand.value_the_cards(),
                                                                     self.players_hand.value_the_cards()))
        elif self.dealers_hand.value_the_cards() < self.players_hand.value_the_cards() < 22:
            print("Dealer's tally: {}. Player wins.".format(self.dealers_hand.value_the_cards()))
        else:
            print("Dealer wins with {}.".format(self.dealers_hand.value_the_cards()))
        return self.dealers_hand.value_the_cards()


