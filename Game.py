import Player


class Game:
    def __init__(self):
        self.number_of_players = None
        self.players = []

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


def welcome_message():
    print("\nWelcome, you can play SushiGo with 2-5 players")

