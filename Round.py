class Round:
    def __int__(self):
        self.maki_rankings = {}

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
