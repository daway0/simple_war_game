from deck import Deck


class Player:
    def __init__(self, player_name):
        self.name = player_name
        self.player_deck = Deck(player_name)

    def __str__(self):
        return self.name

    def give_card(self, cards):
        self.player_deck.add_card(cards)

    def pick_card(self):
        return self.player_deck.pop_card()

    def empty_deck(self):
        return self.player_deck.is_empty()
