from deck import Deck


class Player:
    def __init__(self, player_name):
        self.name = player_name
        self.deck = Deck()

    def __str__(self):
        return self.name

    def give_cards(self, cards):
        self.deck.add_card(cards)

    def pick_card(self):
        return self.deck.pop_card()

    def has_card(self):
        return not self.deck.is_empty()
