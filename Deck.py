import Card
import random


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
            self.cards.append(Card.Card("Dumplings"))
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

    def shuffle(self):
        # set new array
        shuffled_deck = []
        # for each card in the deck
        for i in range(len(self.cards)):
            # pick a random integer between zero and the number of cards left in the deck minus one
            # subtract length of cards array by one due to arrays starting at zero
            random_card_number = random.randint(0, len(self.cards) - 1)
            # append the random card in corresponding randomly chosen position in new deck array
            shuffled_deck.append(self.cards[random_card_number])
            # remove randomly chosen card from existing deck to preserve ratios
            del self.cards[random_card_number]
        # assign existing deck to shuffled deck
        self.cards = shuffled_deck
