from card import Card
import random


class WarGameRule:
    def __init__(self, player1, player2):
        self.__player1 = player1
        self.__player2 = player2

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

    def __create_cards(self):
        # create 52 cards
        self.__cards = []
        for suit in self.__suits:
            for rank in self.__ranks:
                self.__cards.append(Card(suit, rank))

    def __shuffle_cards(self):
        random.shuffle(self.__cards)

    def __divide_cards(self):
        # cards/2
        self.__player1.give_cards(self.__cards[0:26])
        self.__player2.give_cards(self.__cards[26:52])

    def winner(self):
        if not self.__player1.has_card():
            return self.__player2
        if not self.__player2.has_card():
            return self.__player1

        return False

    def value(self, card):
        return self.__ranks[card.rank]

    def configurate(self):
        self.__create_cards()
        self.__shuffle_cards()
        self.__divide_cards()
