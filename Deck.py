import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for i in range(14):
            self.cards.append(Card.Card("Tempura"))
        for i in range(14):
            self.cards.append(Card.Card("Sashimi"))
        for i in range(14):
            self.cards.append(Card.Card("Dumpling"))
        for i in range(12):
            self.cards.append(Card.Card("2 Maki rolls"))
        for i in range(8):
            self.cards.append(Card.Card("3 Maki rolls"))
        for i in range(6):
            self.cards.append(Card.Card("1 Maki rolls"))
        for i in range(10):
            self.cards.append(Card.Card("Salmon Nigiri"))
        for i in range(5):
            self.cards.append(Card.Card("Squid Nigiri"))
        for i in range(5):
            self.cards.append(Card.Card("Egg Nigiri"))
        for i in range(10):
            self.cards.append(Card.Card("Pudding"))
        for i in range(6):
            self.cards.append(Card.Card("Wasabi"))
        for i in range(4):
            self.cards.append(Card.Card("Chopsticks"))

    def show(self):
        for c in self.cards:
            c.show()

