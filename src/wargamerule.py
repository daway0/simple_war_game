from card import Card
from player import Player
import random


class WarGameRule:
    def __init__(self):

        self.__suits = ['diamonds',
                        'hearts',
                        'clubs',
                        'spades']

        self.__ranks = {'1': 1,
                        '2': 2,
                        '3': 3,
                        '4': 4,
                        '5': 5,
                        '6': 6,
                        '7': 7,
                        '8': 8,
                        '9': 9,
                        '10': 10,
                        'jack': 11,
                        'queen': 12,
                        'king': 13}

    def create_cards(self):
        # create 52 cards
        self.cards = []
        for suit in self.__suits:
            for rank in self.__ranks:
                self.cards.append(Card(suit, rank))

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def divide_cards(self, player1, player2):
        # cards/2
        player1.give_card(self.cards[0:26])
        player2.give_card(self.cards[26:52])

    def winner(self, player1, player2):
        if player1.empty_deck():
            return player2
        if player2.empty_deck():
            return player1

        return False

    def value(self, card):
        return self.__ranks[card.rank]


