import random


""" The Card class instanciates a card object.
    The card is assigned a suit and a rank attribute.
    The __repr__ function prints a readable card.
"""
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return " of ".join((self.rank, self.suit))


