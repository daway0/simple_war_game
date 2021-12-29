

class Deck:
    def __init__(self, owner):
        self.owner = owner
        self.deck = []

    def pop_card(self):
        # pick the top
        try:
            return self.deck.pop(0)
        except IndexError:
            print(f'{self.owner}: Deck is empty')
            return False

    def add_card(self, card):
        # add to bottom
        self.deck.extend(card)

    def is_empty(self):
        if self.deck == []:
            return True
        return False

    def display(self):
        for card in self.deck:
            # card (TOP)
            # card
            # card (BOTTOM)
            print(card)
