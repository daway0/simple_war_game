from deck import Deck


class Player:
    def __init__(self, player_name):
        self.__name = player_name
        self.__deck = Deck()

    def __str__(self):
        return self.__name

    def give_cards(self, cards):
        self.__deck.add_card(cards)

    def pick_card(self):
        return self.__deck.pop_card()

    def has_card(self):
        return not self.__deck.is_empty()
