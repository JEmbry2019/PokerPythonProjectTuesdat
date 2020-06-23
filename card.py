import random

""" The Card class

"""
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return " of ".join((self.value, self.suit))



""" The Deck class initiates a deck of cards object each time the game is played.
    When self.cards is called, it creates a complete deck of cards.
    That deck is > 1 it is reordered with shuffle.
"""

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

        # print('This removes a card from the deck') #doesn't print
        # print(self.cards.pop(0))


class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == "A":
                    has_ace = True
                    self.value += 11
                else:
                    self.value += 10

        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def display(self):
        if self.dealer:
            print("hidden")
            print(self.cards[1])
        else:
            for card in self.cards:
                print(card)
            print("Value:", self.get_value())


class Game:
    def __init__(self):
        pass

    def play(self):
        playing = True
        
        while playing:
            self.deck = Deck()
            self.deck.shuffle()

            self.player_hand = Hand()
            self.dealer_hand = Hand(dealer=True)

            for i in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())
            print("Welcome to Blackjack Poker!")
            print("Your hand is:")
            self.player_hand.display()
            print()
            print("Dealer's hand is:")
            self.dealer_hand.display()

            game_over = False

            while not game_over:
                player_has_blackjack, dealer_has_blackjack = self.check_for_blackjack()
                if player_has_blackjack or dealer_has_blackjack:
                    game_over = True
                    self.show_blackjack_results(player_has_blackjack, dealer_has_blackjack)
                    continue

                choice = input("Please choose [Hit / Stick] ").lower()
                while choice not in ["h", "s", "hit", "stick"]:
                    choice = input("Please enter 'hit' or 'stick' (or H/S) ").lower()
                if choice in ['hit', 'h']:
                    self.player_hand.add_card(self.deck.deal())
                    self.player_hand.display()
                    if self.player_is_over():
                        print("You have lost!")
                        game_over = True
                else:
                    player_hand_value = self.player_hand.get_value()
                    dealer_hand_value = self.dealer_hand.get_value()

                    print("Final Results")
                    print("Your hand:", player_hand_value)
                    print("Dealer's hand:", dealer_hand_value)

                    if player_hand_value > dealer_hand_value:
                        print("You Win!")
                    elif player_hand_value == dealer_hand_value:
                        print("Tie!")
                    else:
                        print("Dealer Wins!")
                    game_over = True
            
            again = input("Play Again? [Y/N] ")
            while again.lower() not in ["y", "n"]:
                again = input("Please enter Y or N ")
            if again.lower() == "n":
                print("Thanks for playing!")
                playing = False
            else:
                game_over = False

    def player_is_over(self):
        return self.player_hand.get_value() > 21

    def check_for_blackjack(self):
        player = False
        dealer = False
        if self.player_hand.get_value() == 21:
            player = True
        if self.dealer_hand.get_value() == 21:
            dealer = True

        return player, dealer

    def show_blackjack_results(self, player_has_blackjack, dealer_has_blackjack):
        if player_has_blackjack and dealer_has_blackjack:
            print("Both players have blackjack! Draw!")

        elif player_has_blackjack:
            print("You have blackjack! You win!")

        elif dealer_has_blackjack:
            print("Dealer has blackjack! Dealer wins!")


if __name__ == "__main__":
    g = Game()
    g.play()

# class Card:
#     def __init__(self, suit, value):
#         self.suit = suit
#         self.value = value

#     def __repr__(self):
#             return " of ".join((self.value, self.suit))


# class Deck:
#     def __init__(self):
#         self.cards = [Card(s, v) for s in ["Spades", "Clubs", "Hearts",
#                       "Diamonds"] for v in ["A", "2", "3", "4", "5", "6", 
#                       "7", "8", "9", "10", "J", "Q", "K"]]

#     def shuffle(self):
#         if len(self.cards) > 1:
#             random.shuffle(self.cards)

#     def deal(self):
#         if len(self.cards) > 1:
#             return self.cards.pop(0)



# class Hand:
#     def __init__(self, dealer=False):
#         self.dealer = dealer
#         self.cards = []
#         self.value = 0

#     def add_card(self, card):
#         self.cards.append(card)


#     def calculate_value(self):
#         self.value = 0
#         has_ace = False
#         for card in self.cards:
#             if card.value.isnumeric():
#                 self.value += int(card.value)
#             else:
#                 if card.value == "A":
#                     has_ace = True
#                     self.value += 11
#                 else:
#                     self.value += 10

#         if has_ace and self.value > 21:
#             self.value -= 10

#     def get_value(self):
#         self.calculate_value()
#         return self.value




#     def display(self):
#         if self.dealer:
#             print("hidden")
#             print(self.cards[1])
#         else:
#             for card in self.cards:
#                 print(card)
#             print("Value:", self.get_value())




# class Game:
#     def __init__(self):
#         pass

#     def play(self):
#         playing = True

#         while playing:
#             self.deck = Deck()
#             self.deck.shuffle()

#             self.player_hand = Hand()
#             self.dealer_hand = Hand(dealer=True)

#             for i in range(2):
#                 self.player_hand.add_card(self.deck.deal())
#                 self.dealer_hand.add_card(self.deck.deal())

#             print("Your hand is:")
#             self.player_hand.display()
#             print()
#             print("Dealer's hand is:")
#             self.dealer_hand.display()


#         choice = input("Please choose [Hit / Stick] ").lower()
#         while choice not in ["h", "s", "hit", "stick"]:
#                     choice = input("Please enter 'hit' or 'stick' (or H/S) ").lower()

#         if choice in ['hit', 'h']:
#                     self.player_hand.add_card(self.deck.deal())
#                     self.player_hand.display()

#                     if self.player_is_over():
#                         print("You have lost!")
#                         game_over = True

#                     else:
#                         player_hand_value = self.player_hand.get_value()
#                     dealer_hand_value = self.dealer_hand.get_value()

#                     print("Final Results")
#                     print("Your hand:", player_hand_value)
#                     print("Dealer's hand:", dealer_hand_value)

#                     if player_hand_value > dealer_hand_value:
#                         print("You Win!")
#                     elif player_hand_value == dealer_hand_value:
#                         print("Tie!")
#                     else:
#                         print("Dealer Wins!")
#                     game_over = True


#         again = input("Play Again? [Y/N] ")
#         while again.lower() not in ["y", "n"]:
#                 again = input("Please enter Y or N ")
#         if again.lower() == "n":
#             print("Thanks for playing!")
#             playing = False
#         else:
#                 game_over = False




#     def player_is_over(self):
#         return self.player_hand.get_value() > 21


#         game_over = False

#         while not game_over:
#                 player_has_blackjack, dealer_has_blackjack = self.check_for_blackjack()


#                 if player_has_blackjack or dealer_has_blackjack:
#                     game_over = True
#                     self.show_blackjack_results(
#                         player_has_blackjack, dealer_has_blackjack)
#                     continue


#     def check_for_blackjack(self):
#         player = False
#         dealer = False
#         if self.player_hand.get_value() == 21:
#             player = True
#         if self.dealer_hand.get_value() == 21:
#             dealer = True

#         return player, dealer


#     def show_blackjack_results(self, player_has_blackjack, dealer_has_blackjack):
#         if player_has_blackjack and dealer_has_blackjack:
#             print("Both players have blackjack! Draw!")

#         elif player_has_blackjack:
#             print("You have blackjack! You win!")

#         elif dealer_has_blackjack:
#             print("Dealer has blackjack! Dealer wins!")



# if __name__ == "__main__":
#     game = Game()
#     game.play()




# class Deck:

#     def __init__(self):
#         self.suit = ["Hearts", "Clubs", "Spades", "Diamonds"]
#         self.val = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}
#         self.deck = []

#     def make_deck(self):
#         for s in self.suit:
#             for v in self.val:
#                 self.deck.append(v + " of " + s)
#         return random.shuffle(self.deck)

#     def give_player_one(self):
#         card = self.deck.pop()
#         return card

#     def give_dealer_one(self):
#         card = self.deck.pop()
#         return card

#     def create_player_hand(self):
#         hand = []
#         for card in range(2):
#             hand.append(self.give_player_one())
#         return hand

#     def create_dealer_hand(self):
#         hand = []
#         for card in range(2):
#             hand.append(self.give_dealer_one())
#         return hand


#     def get_player_hand_value(self, hand):
#        d = 0
#        for card in hand:
#            for value in card[0]:
#                try:
#                    value = int(value)
#                    if int(value) == 1:
#                        value = 10
#                except ValueError:
#                    if value == 'A':
#                        value = 11
#                    elif value in 'JQK':
#                        value = 10
#            d += int(value)
#        return d

#     def get_dealer_hand_value(self, hand):
#        d = 0
#        for card in hand:
#            for value in card[0]:
#                try:
#                    value = int(value)
#                    if int(value) == 1:
#                        value = 10
#                except ValueError:
#                    if value == 'A':
#                        value = 11
#                    elif value in 'JQK':
#                        value = 10
#            d += int(value)
#        return d


#     def get_player_single_value(self, card):
#         d = 0
#         for value in card[0]:
#             try:
#                 value = int(value)
#                 if int(value) == 1:
#                     value = 10
#             except ValueError:
#                 if value == 'A':
#                     value = 11

#                 elif value in 'JQK':
#                     value = 10
#         d += int(value)
#         return d

#     def get_dealer_single_value(self, card):
#         d = 0
#         for value in card[0]:
#             try:
#                 value = int(value)
#                 if int(value) == 1:
#                     value = 10
#             except ValueError:
#                if value == 'A':
#                    value = 11
#                elif value in 'JQK':
#                    value = 10
#         d += int(value)
#         return d

# deck = Deck()