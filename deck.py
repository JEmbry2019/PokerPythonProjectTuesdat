import random
from card import Card
from hand import Hand

# class Deck:
#     def __init__(self):
#         self.card = [Card(s, v) for s in ["Spades", "Clubs", "Hearts", "Diamonds"] for v in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]

#         print('This is the deck')
#         print(self.card)

#     def shuffle(self):
#         if len(self.card) > 1:
#             random.shuffle(self.card)

#         print('This is the Shuffled deck')
#         print(self.card)

#     def deal(self):
#         if len(self.card) > 1:
#             return self.card.pop(0)




class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in ["Spades", "Clubs", "Hearts", "Diamonds"] for v in
                      ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]
        print('This is the deck')
        print(self.cards)

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)
        print('This is the Shuffled deck')
        print(self.cards)

    def deal(self):
        if len(self.cards) > 1:
           return self.cards.pop(0)

        print('This removes a card from the deck') #doesn't print
        print(self.cards.pop(0))