import random
from card import Card
from hand import Hand


""" The Deck class instanciates a deck of cards object each time the game is played.
    When we pass self.cards to the Card class, and use list comprehension to loop over the suit and rank lists 
    and creates a complete deck of cards.
    If the deck is > 1 it is reordered with shuffle ( a deck with 1 or less cards cannot be suffled).
    The pop method removes the card at index 0 and that card is returned.
"""


class Deck:
    def __init__(self):
        self.cards = [Card(s, r) for s in ["Spades", "Clubs", "Hearts", "Diamonds"] for r in
                      ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]
        print('This is the deck')
        print(self.cards)
    # This method puts the cards list in random order.
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)
        print('This is the Shuffled deck')
        print(self.cards)

    def deal(self):
        if len(self.cards) > 1:
           return self.cards.pop(0)

