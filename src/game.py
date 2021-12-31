from player import Player
from wargamerule import WarGameRule


class Game:
    def __init__(self, player1_name, player2_name):
        self.__player1 = Player(player1_name)
        self.__player2 = Player(player2_name)
        self.__rule = WarGameRule(self.__player1, self.__player2)
        self.__rule.configuration()
        self.__ground = []
        self.__round = 1

    def __empty_ground(self):
        self.__ground = []

    def start(self):
        while not self.__rule.winner(self.__player1, self.__player2):

            card1 = self.__player1.pick_card()
            card2 = self.__player2.pick_card()
            self.__ground.append(card1)
            self.__ground.append(card2)

            if self.__rule.value(card1) > self.__rule.value(card2):

                self.__player1.give_cards(self.__ground)
                self.__round += 1

                for card in self.__ground:
                    print(card)
                print(f'to {self.__player1}')
                print('--------------')
                self.__empty_ground()

            elif self.__rule.value(card1) < self.__rule.value(card2):
                self.__player2.give_cards(self.__ground)
                self.__round += 1
                for card in self.__ground:
                    print(card)
                print(f'to {self.__player2}')
                print('--------------')
                self.__empty_ground()

            elif self.__rule.value(card1) == self.__rule.value(card2):

                for count in range(self.__rule.value(card1)):
                    if self.__rule.winner(self.__player1, self.__player2):
                        print(f'{self.__round} rounds')
                        return self.__rule.winner(self.__player1, self.__player2)
                    else:
                        self.__ground.append(self.__player1.pick_card())
                        self.__ground.append(self.__player2.pick_card())
        print(f'{self.__round} rounds')
        return self.__rule.winner(self.__player1, self.__player2)


game = Game('Erfan', 'computer')
result = game.start()
print(result)
