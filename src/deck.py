

class Deck:
    def __init__(self):
        self.__data = []

    def pop_card(self):
        # pick the top
        return self.__data.pop(0)

    def add_card(self, card):
        # add to bottom
        self.__data.extend(card)

    def is_empty(self):
        if self.__data == []:
            return True
        return False

    def display(self):
        for card in self.__data:
            # card (TOP)
            # card
            # card (BOTTOM)
            print(card)
