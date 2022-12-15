import Card
import Deck
import Player

new_deck = Deck.Deck()
new_deck.show()
print("\n {} card in the deck".format(len(new_deck.deck)))

new_deck.shuffle()
new_deck.show()
print("\n {} card in the deck".format(len(new_deck.deck)))

new_deck.shuffle()
new_deck.show()
print("\n {} card in the deck".format(len(new_deck.deck)))

print("\nWelcome, you can play SushiGo with 2-5 players")
player_number = int(input("\nPlease enter the number of players:"))
players = []
for i in range(player_number):
    players.append(Player.Player("Player {}".format(i + 1), i + 1))

for player in players:
    print(player.name)
    print(player.score)

# deal cards for round one based on number of players
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


print("{} cards in the deck now".format(len(new_deck.deck)))
for player in players:
    print("\nPlayer {}'s hand for round 1".format(player.number))
    player.show_hand()

Player.pass_hand(players)

for player in players:
    print("\nPlayer {}'s hand after passing".format(player.number))
    player.show_hand()





