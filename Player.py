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
            if c == "Pudding":
                self.puddings += 1
            elif c == "Sashimi":
                sashimi += 1
            elif c == "Tempura":
                tempura += 1
            elif c == "Dumplings":
                dumplings += 1
            elif c == "Wasabi":
                wasabi += 1
            elif c == "Squid Nigiri":
                if wasabi > 0:
                    nigiri += (3 * 3)
                    wasabi -= 1
                else:
                    nigiri += 3
            elif c == "Salmon Nigiri":
                if wasabi > 0:
                    nigiri += (3 * 2)
                    wasabi -= 1
                else:
                    nigiri += 2
            elif c == "Egg Nigiri":
                if wasabi > 0:
                    nigiri += (3 * 1)
                    wasabi -= 1
                else:
                    nigiri += 1
            elif c == "3 Maki rolls":
                maki += 3
            elif c == "2 Maki rolls":
                maki += 2
            elif c == "1 Maki rolls":
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











