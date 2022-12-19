import Card
import math


def pass_hand(players):
    player_num = len(players)
    last_player_hand = players[player_num - 1].hand
    for i in range(player_num - 1):
        players[i + 1].hand = players[i].hand
    players[0].hand = last_player_hand


class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.cards = []
        self.hand = []
        self.score = 0
        self.puddings = 0
        self.maki = 0

    def show_hand(self):
        for c in self.hand:
            c.show()

    def show_cards(self):
        for c in self.cards:
            c.show()

    def score_cards(self):
        maki = 0
        tempura = 0
        sashimi = 0
        dumplings = 0
        wasabi = 0
        nigiri = 0
        for c in self.cards:
            if c.card_type == "Pudding":
                self.puddings += 1
            elif c.card_type == "Sashimi":
                sashimi += 1
            elif c.card_type == "Tempura":
                tempura += 1
            elif c.card_type == "Dumplings":
                dumplings += 1
            elif c.card_type == "Wasabi":
                wasabi += 1
            elif c.card_type == "Squid Nigiri":
                if wasabi > 0:
                    nigiri += (3 * 3)
                    wasabi -= 1
                else:
                    nigiri += 3
            elif c.card_type == "Salmon Nigiri":
                if wasabi > 0:
                    nigiri += (3 * 2)
                    wasabi -= 1
                else:
                    nigiri += 2
            elif c.card_type == "Egg Nigiri":
                if wasabi > 0:
                    nigiri += (3 * 1)
                    wasabi -= 1
                else:
                    nigiri += 1
            elif c.card_type == "3 Maki rolls":
                maki += 3
            elif c.card_type == "2 Maki rolls":
                maki += 2
            elif c.card_type == "1 Maki rolls":
                maki += 1
        self.maki = maki
        self.score += ((tempura // 2) * 5)
        self.score += ((sashimi // 3) * 10)
        if dumplings == 1:
            self.score += 1
        if dumplings == 2:
            self.score += 3
        if dumplings == 3:
            self.score += 6
        if dumplings == 4:
            self.score += 10
        if dumplings >= 5:
            self.score += 15
        self.score += nigiri

    def choose_a_card(self):
        print("\nHere is your hand player {}: ".format(self.number))
        self.show_hand()
        print("\nHere are your cards: ")
        self.show_cards()
        input_correct = False
        counter = 0
        card_choice = None
        while not input_correct:
            if counter != 0:
                print("\nI'm sorry, that input wasn't correct, please type your card again.")
            print("\nWhich card would you like to take from your hand and add to your cards?")
            card_input = input()
            for card in self.hand:
                if card.card_type.lower() == card_input.lower():
                    input_correct = True
                    card_choice = card
                    break
            counter += 1
        self.cards.append(card_choice)
        self.hand.remove(card_choice)
