import Deck
import Player
import Round
import Game

# Start game
game = Game.Game()

# Initialize and shuffle deck of cards
card_deck = Deck.Deck()
card_deck.shuffle()

# Start first round
round_one = Round.Round()

# Welcome message 
Game.welcome_message()
game.get_number_players()

# deal cards for round one based on number of players
round_one.deal_starting_hand(game.players, card_deck)

# add card from hand to personal pile and pass remaining cards in hand until all cards are gone
game.play_round()

# score round
round_one.score_without_maki(game.players)
# score maki
round_one.score_maki(game.players)

# display score
game.display_scores()

# after all three rounds, score pudding





