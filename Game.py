import Player


class Game:
    def __init__(self):
        self.number_of_players = None
        self.players = []
        self.sorted_puddings = None
        self.points_added_for_most_puddings = 6
        self.points_subtracted_for_least_puddings = 6
        self.players_with_most_puddings = 0
        self.players_with_least_puddings = 0

    def get_number_players(self):
        player_number = int(input("\nPlease enter the number of players:"))
        for i in range(player_number):
            self.players.append(Player.Player("Player {}".format(i + 1), i + 1))

    def play_round(self):
        # add card from hand to personal pile and pass remaining cards in hand until all cards are gone
        # TODO: check that all players hands are empty (more than two players)
        while len(self.players[0].hand) != 0 and len(self.players[1].hand) != 0:
            for player in self.players:
                player.choose_cards()
            Player.pass_hand(self.players)
            for player in self.players:
                print("\nPlayer {}'s hand after passing".format(player.number))
                player.show_hand()

    def display_scores(self):
        for player in self.players:
            print("\nPlayer {0}'s score: {1}".format(player.number, player.score))

    def sort_puddings(self):
        player_puddings = []
        for player in self.players:
            player_puddings.append(player.puddings)
        self.sorted_puddings = sorted(player_puddings, reverse=True)

    def points_for_most_puddings(self):
        for player in self.players:
            if player.puddings == self.sorted_puddings[0]:
                self.players_with_most_puddings += 1
        self.points_added_for_most_puddings //= self.players_with_most_puddings

    def points_for_least_puddings(self):
        if len(self.players) == 2:
            self.points_subtracted_for_least_puddings = 0
        for player in self.players:
            if player.puddings == self.sorted_puddings[-1]:
                self.players_with_least_puddings += 1
        self.points_subtracted_for_least_puddings //= self.players_with_least_puddings

    def score_puddings(self):
        # only award points for most pudding in two player game, don't take away points from least puddings player
        self.sort_puddings()
        self.points_for_most_puddings()
        self.points_for_least_puddings()

        if self.sorted_puddings[0] == 0:
            return

        for player in self.players:
            if player.puddings == self.sorted_puddings[0]:
                player.score += self.points_added_for_most_puddings
            elif player.puddings == self.sorted_puddings[-1]:
                player.score -= self.points_subtracted_for_least_puddings


def welcome_message():
    print("\nWelcome, you can play SushiGo with 2-5 players")
