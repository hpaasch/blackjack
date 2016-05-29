from deck import Deck


class Hand:

    def __init__(self):
        self.cards_in_hand = []
        self.deck = Deck()

    def initial_deal(self):
        for _ in range(2):
            new_cards = Deck.deal_one_card(self.deck)
            self.cards_in_hand.append(new_cards)
        print(self.cards_in_hand)



heptest = Hand()
heptest.initial_deal()

