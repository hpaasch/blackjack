from player import Player
from deck import Deck


class Hand:

    def __init__(self):
        self.cards_in_hand = []
        self.deck = Deck()

        # self.player_one = Player()
        # self.dealer = Player()
        # self.deck = Deck()
        # self.player_one.hand_total = 0  # self.deck.value_the_cards()  # self.player.hold_cards()
        # self.player_one.cards = self.player_one.cards_in_hand
        # self.dealer.hand_total = 0  # self.dealer.hand_total  # self.deck.value_the_cards()

    def initial_deal(self):
        new_cards = (Deck.deal_one_card(self.deck) for _ in range(2))
        self.cards_in_hand.append(new_cards)
        print(self.cards_in_hand)
        return new_cards

    def __str__(self):
        return ' '.join(self.cards_in_hand)

    def draw_a_card(self):
        new_card = Deck.deal_one_card()


    def players_hand(self):
        while self.player_one.hand_total < 21:
            hit = input("Hit or Stay? H/S ").lower()
            if hit == 'h':
                new_card = Deck.deal_one_card(self.deck)
                self.player_one.cards_in_hand.append(new_card)
                # Deck.deal_one_card(self.deck)
                print("Player's hand now holds: ", self.player_one.cards_in_hand)
                # self.player_one.hand_total = Deck.value_the_cards(self.deck)
                new_value = Deck.value_the_cards(self.deck)
                self.player_one.hand_total = new_value
                # self.player_one.hand_total = self.deck.value_the_cards()
                print("Player's cards tally: ", self.player_one.hand_total)
                if self.player_one.hand_total > 21:
                    print("Player's hand is a bust.")
            else:
                print("Player's cards tally: ", self.player_one.hand_total)
                break
        player_total = self.player_one.hand_total
        return player_total

    def dealers_hand(self):
        while self.dealer.hand_total < 17:
            Deck.deal_one_card(self.deck)
            print("Dealer hand now holds: ", self.dealer.cards_in_hand)
            self.player_one.hand_total = self.deck.value_the_cards()
            print("Dealer's cards tally: ", self.dealer.hand_total)
        if self.dealer.hand_total > 21:
            print("Dealer's hand is bust at {}.".format(self.dealer.hand_total))
        else:
            print("Dealer's hand: ", self.dealer.hand_total)
        dealer_total = self.dealer.hand_total
        return dealer_total

hep_test = Hand()
hep_test.initial_deal()
hep_test.players_hand()
