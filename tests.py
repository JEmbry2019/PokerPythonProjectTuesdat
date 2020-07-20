import unittest
import card
import hand
import game
import deck

from card import Card
from deck import Deck
from hand import Hand
from game import Game




class HandTestCase(unittest.TestCase):

    def test_add_card_construction(self):
        cards = Card(8, 'Clubs')

        self.assertEqual(cards.rank, 'Clubs')
        self.assertEqual(cards.suit, 8)


# class HandTestCase(unittest.TestCase):
#     def test_three_kings_is_bust(self):
#         hand = Hand()
#         hand.add_card(Card(13, Card.SPADES))
#         hand.add_card(Card(13, Card.HEARTS))
#         hand.add_card(Card(13, Card.CLUBS))

#         self.assertTrue(hand.is_bust())

#  def player_is_over(self):
#         return self.player_hand.get_rank() > 21

# class GameTestCase(unittest.TestCase):
#     def test_player_is_over_21(self):
#         game = Game()

#         game.player_hand.add_card(Hand(13, Hand.Hearts))
#         game.player_hand.add_card(Hand(13, Hand.Clubs))


#         return self.player_hand.get_rank() > 21



if __name__ == '__main__':
    unittest.main()
