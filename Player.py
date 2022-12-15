import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.hand = []
        self.score = 0
        self.puddings = 0

    def show_hand(self):
        for c in self.hand:
            c.show()
