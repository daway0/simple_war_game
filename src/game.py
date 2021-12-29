from player import Player
from wargamerule import WarGameRule
import sys
sys.stdout = open('output.txt', 'w')


class Game:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.rule = WarGameRule()
        self.rule.create_cards()
        self.rule.shuffle_cards()
        self.rule.divide_cards(self.player1, self.player2)
        self.ground = []

        while not self.rule.winner(self.player1, self.player2):

            card1 = self.player1.pick_card()
            card2 = self.player2.pick_card()
            self.ground.append(card1)
            self.ground.append(card2)

            if self.rule.value(card1) > self.rule.value(card2):

                self.player1.give_card(self.ground)
                for card in self.ground:
                    print(card)
                print(f'to {self.player1}')
                print('--------------')
                self.ground = []

            elif self.rule.value(card1) < self.rule.value(card2):
                self.player2.give_card(self.ground)
                for card in self.ground:
                    print(card)
                print(f'to {self.player2}')
                print('--------------')
                self.ground = []

            elif self.rule.value(card1) == self.rule.value(card2):

                for count in range(self.rule.value(card1)):
                    if self.player1.empty_deck() or self.player2.empty_deck():
                        print(self.rule.winner(self.player1, self.player2))
                        sys.exit()
                    else:
                        self.ground.append(self.player1.pick_card())
                        self.ground.append(self.player2.pick_card())
        print(self.rule.winner(self.player1, self.player2))


game1 = Game('Erfan', 'computer')
