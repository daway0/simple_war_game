
class Card:
    def __init__(self, suit, rank):
        self.suit = str(suit)
        self.rank = str(rank)

    def __str__(self):
        return (self.rank + ' of ' + self.suit)
