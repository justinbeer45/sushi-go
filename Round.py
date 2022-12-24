class Round:
    def __int__(self):
        self.maki_rankings = {}

    def deal_starting_hand(self, players, new_deck):
        player_number = len(players)
        if player_number == 2:
            for i in range(10):
                for player in players:
                    player.hand.append(new_deck.deck[0])
                    del new_deck.deck[0]
        if player_number == 3:
            for i in range(9):
                for player in players:
                    player.hand.append(new_deck.deck[0])
                    del new_deck.deck[0]
        if player_number == 4:
            for i in range(8):
                for player in players:
                    player.hand.append(new_deck.deck[0])
                    del new_deck.deck[0]
        if player_number == 5:
            for i in range(7):
                for player in players:
                    player.hand.append(new_deck.deck[0])
                    del new_deck.deck[0]

    def score_maki(self, players):
        players_with_most_maki_rolls = 0
        points_for_most_maki = 6
        players_with_second_most_maki_rolls = 0
        points_for_second_most_maki = 3
        player_maki_rolls = []
        for player in players:
            player_maki_rolls.append(player.maki)
        sorted_maki_rolls = sorted(player_maki_rolls, reverse=True)
        if sorted_maki_rolls[0] == 0:
            return
        for player in players:
            if player.maki == sorted_maki_rolls[0]:
                players_with_most_maki_rolls += 1
        points_for_most_maki //= players_with_most_maki_rolls
        for player in players:
            if player.maki == sorted_maki_rolls[0]:
                player.score += points_for_most_maki
        if players_with_most_maki_rolls > 1:
            return
        else:
            for player in players:
                if player.maki == sorted_maki_rolls[1]:
                    players_with_second_most_maki_rolls += 1
            points_for_second_most_maki //= players_with_second_most_maki_rolls
            for player in players:
                if player.maki == sorted_maki_rolls[1]:
                    player.score += points_for_second_most_maki

    def score_without_maki(self, players):
        for player in players:
            # score each player (excluding maki scoring which is done below
            player.score_cards()





