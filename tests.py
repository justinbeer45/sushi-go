import unittest
import Deck
import Game
import Player
import Round
import Card


class TestSushiGo(unittest.TestCase):

    def setUp(self):
        self.card_deck = Deck.Deck()

    def test_cards_in_deck(self):
        card_distribution = {
            "Tempura": [14, 0],
            "Dumplings": [14, 0],
            "2 Maki rolls": [12, 0],
            "3 Maki rolls": [8, 0],
            "1 Maki rolls": [6, 0],
            "Salmon Nigiri": [10, 0],
            "Squid Nigiri": [5, 0],
            "Egg Nigiri": [5, 0],
            "Pudding": [10, 0],
            "Wasabi": [6, 0],
            "Chopsticks": [4, 0],
        }
        for c in self.card_deck.cards:
            for d in card_distribution.items():
                if c.card_type == d[0]:
                    d[1][1] += 1
        for d in card_distribution.items():
            self.assertEqual(d[1][0], d[1][1], "Unequal card number for {}".format(d[0]))


if __name__ == '__main__':
    unittest.main()
