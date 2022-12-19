import Card
import Deck
import Player
import Round

round_one = Round.Round()

new_deck = Deck.Deck()
new_deck.show()
print("\n {} cards in the deck".format(len(new_deck.deck)))

new_deck.shuffle()
new_deck.show()
print("\n {} cards in the deck".format(len(new_deck.deck)))

new_deck.shuffle()
new_deck.show()
print("\n {} cards in the deck".format(len(new_deck.deck)))

print("\nWelcome, you can play SushiGo with 2-5 players")
player_number = int(input("\nPlease enter the number of players:"))
players = []
for i in range(player_number):
    players.append(Player.Player("Player {}".format(i + 1), i + 1))

for player in players:
    print(player.name)
    print(player.score)

# deal cards for round one based on number of players
round_one.deal_starting_hand(players, new_deck)
print("\n Deck cards after dealing:")
new_deck.show()
print("\n {} cards in the deck".format(len(new_deck.deck)))


print("{} cards in the deck now".format(len(new_deck.deck)))
for player in players:
    print("\nPlayer {}'s starting hand".format(player.number))
    player.show_hand()

while len(players[0].hand) != 0:
    for player in players:
        player.choose_a_card()
    Player.pass_hand(players)
    for player in players:
        print("\nPlayer {}'s hand after passing".format(player.number))
        player.show_hand()

for player in players:
    print("\nPlayer {}'s cards:".format(player.number))
    player.show_cards()
    # score each player (excluding maki scoring which is done below
    player.score_cards()
    print("\nPlayer {}'s score before maki counting".format(player.number))
    print(player.score)
    print("\nPlayer {}'s maki roll count".format(player.number))
    print(player.maki)

# score maki
round_one.score_maki(players)
for player in players:
    print("\nPlayer {}'s score after maki counting".format(player.number))
    print(player.score)




