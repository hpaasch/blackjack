from player import Player
from deck import Deck


class Hand:

    def __init__(self):
        self.player_one = Player()
        self.dealer = Player()
        self.deck = Deck()
        self.player_one.hand_total = 0  # self.deck.value_the_cards()  # self.player.hold_cards()
        # self.player_one.deal_in = self.deck.initial_deal()
        # self.dealer.deal_in = self.deck.initial_deal()
        self.dealer.hand_total = 0  # self.dealer.hand_total  # self.deck.value_the_cards()

        print(">" * 40)
        # print("Player's hand opens with: ", self.player_one.deal_in)
        print("Player's hand opening value: ", self.player_one.hand_total)
        # print("Dealer reveals both for testing: ", self.dealer.deal_in)
        # print("Dealer reveals one up: ", self.dealer.deal_in[0])

    def initial_deal(self):
        self.player_one.cards_in_hand.append(self.deck.initial_deal())
        print("Player's initial deal is these cards: ", self.player_one.cards_in_hand)
        self.player_one.hand_total = self.deck.value_the_cards()
        print("Player's cards tally: ", self.player_one.hand_total)
        # self.dealer.cards_in_hand = self.deck.initial_deal()
        # print("Dealer's initial deal is these cards: ", self.player_one.cards_in_hand)
        return self.player_one.hand_total

    def players_hand(self):
        while self.player_one.hand_total < 21:
            hit = input("Hit or Stay? H/S ").lower()
            if hit == 'h':
                Deck.deal_one_card(self.deck)
                print("Player hand now holds: ", self.player_one.cards_in_hand)
                self.player_one.hand_total = self.deck.value_the_cards()
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
        if self.dealer.hand_total > 21:
            print("Dealer's hand is bust at {}.".format(self.dealer.hand_total))
        else:
            print("Dealer's hand: ", self.dealer.hand_total)
        dealer_total = self.dealer.hand_total
        return dealer_total

hep_test = Hand()
hep_test.initial_deal()
hep_test.players_hand()
