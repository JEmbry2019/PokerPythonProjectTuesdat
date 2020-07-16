import unittest
import card
import hand
import game
import deck

from card import Card
from deck import Deck
from hand import Hand
from game import Game




class GameTestCase(unittest.TestCase):
        # def test_add(self):
        #     result = calculation.add(10, 5)
        #     self.assertEqual(result, 15)

    def test_check_for_blackjack(self):
        player = False
        dealer = False
        if self.player_hand.get_rank() == 21:
            player = True
        if self.dealer_hand.get_rank() == 21:
            dealer = True
        self.assertTrue(player_hand.get_rank(21))
        return player, dealer

    def test_five_plus_five(self):
            assert 5 + 5 == 10


#     def test_player_is_over(self):
#         game = Game()
#         player_hand = 22
#         self.assertEqual(player_hand(), 22)



# class DeckTestCase(unittest.TestCase):
#     def test_initial_deck_has_52_cards(self):
#         deck = Deck()

#         self.assertEqual(len(deck.cards), 52)

if __name__ == '__main__':
    unittest.main()
