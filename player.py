# creates player's hand
# creates dealer's hand
# plays out player's hand
# plays out dealer's hand

from hand import Hand
from deck import Deck


class PlayTheHands:
    def __init__(self):
        self.deck = Deck()
        self.players_hand = Hand()
        self.dealers_hand = Hand()

    def opening(self):
        Hand.initial_deal(self.players_hand)
        Hand.initial_deal(self.dealers_hand)
        print("Dealer showing: ", self.dealers_hand)  # need to hide one
        print("Player showing: ", self.players_hand)
        print("Player's cards tally: ", self.players_hand.value_the_cards())

    def players_logic(self):
        while self.players_hand.value_the_cards() < 21:
            hit = input("Hit or Stay? H/S ").lower()
            if hit == 'h':
                Hand.draw_a_card(self.players_hand)
                print("Player holding: ", self.players_hand)
                print("Player's cards tally: ", self.players_hand.value_the_cards())  # for testing
                if self.players_hand.value_the_cards() > 21:
                    print("Player's hand is a bust.")
            else:
                print("Player's cards tally: ", self.players_hand.value_the_cards())
                break
        player_total = self.players_hand.value_the_cards()
        return player_total

    def dealers_logic(self):
        print("Dealer showing both now: ", self.dealers_hand)
        while self.dealers_hand.value_the_cards() < 17:
            Hand.draw_a_card(self.dealers_hand)
            print("Dealer takes a card: ", self.dealers_hand)
        if self.dealers_hand.value_the_cards() > 21:
            print("Dealer's hand is bust at {}.".format(self.dealers_hand.value_the_cards()))
        else:
            print("Dealer's cards tally: ", self.dealers_hand.value_the_cards())
        dealer_total = self.dealers_hand.value_the_cards()
        return dealer_total


heptest = PlayTheHands()
heptest.opening()
heptest.players_logic()
heptest.dealers_logic()




