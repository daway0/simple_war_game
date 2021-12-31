

class Deck:
    def __init__(self):
        self.data = []

    def pop_card(self):
        # pick the top
        return self.data.pop(0)

    def add_card(self, card):
        # add to bottom
        self.data.extend(card)

    def is_empty(self):
        if self.data == []:
            return True
        return False

    def display(self):
        for card in self.data:
            # card (TOP)
            # card
            # card (BOTTOM)
            print(card)
