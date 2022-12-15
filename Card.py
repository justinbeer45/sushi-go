class Card:
    def __init__(self, card_type):
        self.card_type = card_type

    def show(self):
        print("{}".format(self.card_type))
