import unittest
import Deck
import Game
import Player
import Round


class TestDeck(unittest.TestCase):
    def test_cards_in_deck(self):
        tempura_cards = 0
        deck_of_cards = Deck.Deck()
        for c in deck_of_cards.deck:
            if c.card_type == "Tempura":
                tempura_cards += 1
        self.assertEqual(tempura_cards, 14, "There are not 14 Tempura cards in a new deck")  # add assertion here

    def test_number_of_cards(self):
        deck_of_cards = Deck.Deck()
        cards_in_deck = len(deck_of_cards.deck)
        self.assertEqual(cards_in_deck, 108, "There are not 108 cards in the deck.")

    def test_passing_hand(self):
        # Initialize and shuffle deck of cards
        card_deck = Deck.Deck()
        card_deck.shuffle()
        # Initialize round
        round_one = Round.Round()
        # Initialize players
        players = []
        for i in range(2):
            players.append(Player.Player("Player {}".format(i + 1), i + 1))
        hand_for_player_one = []
        for i in range(0, 20, 2):
            hand_for_player_one.append(card_deck.deck[i])
        hand_for_player_two = []
        for i in range(1, 20, 2):
            hand_for_player_two.append(card_deck.deck[i])
        # deal cards for round one based on number of players
        round_one.deal_starting_hand(players, card_deck)
        self.assertEqual(len(card_deck.deck), 88, "Wrong number of cards after dealing to two players")

        for i in range(10):
            self.assertEqual(players[0].hand[i].card_type, hand_for_player_one[i].card_type, "not the same cards")
        for i in range(10):
            self.assertEqual(players[1].hand[i].card_type, hand_for_player_two[i].card_type, "not the same cards")

        # pass cards
        Player.pass_hand(players)
        for i in range(10):
            self.assertEqual(players[0].hand[i].card_type, hand_for_player_two[i].card_type, "not the same cards")
        for i in range(10):
            self.assertEqual(players[1].hand[i].card_type, hand_for_player_one[i].card_type, "not the same cards")


if __name__ == '__main__':
    unittest.main()
