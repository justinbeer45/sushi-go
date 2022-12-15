import Card

def pass_hand(players):
    player_num = len(players)
    last_player_hand = players[player_num - 1].hand
    print("Player {}'s hand:".format(player_num))
    players[player_num - 1].show_hand()
    for i in range(player_num - 1):
        players[i + 1].hand = players[i].hand
    players[0].hand = last_player_hand
    for j in range(player_num):
        print("Player {}'s hand:".format(j + 1))
        players[j].show_hand()



class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.cards = []
        self.hand = []
        self.score = 0
        self.puddings = 0

    def show_hand(self):
        for c in self.hand:
            c.show()
