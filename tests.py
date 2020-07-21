import unittest

from card import Card
from deck import Deck
from hand import Hand
from game import Game

""" This file contains 3 tests.
    Tested are the add_card(), calculate_rank(), and the deal() functions.
    Some print statements were added for clearity.

"""


class HandTestCase(unittest.TestCase):


    
#  # Test 1 -A Card object is added to the cards list.
    def test_add_card(self):

        hand = Hand()
        self.cards = []
        initial_size = len(hand.cards)
        print(initial_size)
        hand.add_card(self)
        size = len(hand.cards)
        print(size)

        self.assertEqual(size, initial_size + 1)


#----------------------------------------------        

    # def test_add_card_construction(self):
    #     cards = Card(8, 'Clubs')

    #     self.assertEqual(cards.rank, 'Clubs')
    #     self.assertEqual(cards.suit, 8)


# ---------------------------------

# Test 2 - This function calculates rank correctly.   
    def test_calculate_rank(self):

        hand = Hand()
        self.rank = 'Q'
        hand.calculate_rank()
       
        self.assertTrue(self.rank, 12)




#-------------------------------------

# Test 3 This function makes sure the deck has more than 1 card.
class DeckTestCase(unittest.TestCase):

    def test_deal_checks_deck_greater_than_1(self):
        deck = Deck()
        initial_size = len(deck.cards)
        print(initial_size)
        deck.deal()

        self.assertGreater(len(deck.cards), 2)

        


if __name__ == '__main__':
    unittest.main()
