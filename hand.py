""" The Hand class instantiates a list of Card objects.
    We add a card to a hand by adding a Card instanse to the cards list.
    To calculate the value, we determine if card is numeric, Ace, or other (a face card).
    Once determined the value is added.
    If the hand is a bust (>21), the value of the Ace is reduced to 1.
"""


class Hand:
    # This function when called from the game class creates a empty hand for the player then the dealer.
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.rank = 0

    # A Card object is added to the cards list.
    def add_card(self, card):
        self.cards.append(card)
    # This function initiates the card at 0 value and not an ace.  
    def calculate_rank(self):
        self.rank = 0
        has_ace = False
        # Here we loop througe the Card instances, calculate and add the value.
        for card in self.cards:
            if card.rank.isnumeric():
                self.rank += int(card.rank)
            else:
                if card.rank == "A":
                    has_ace = True
                    self.rank += 11
                else:
                    self.rank += 10
         # If over 21 Ace rank drops from 11 to 1
        if has_ace and self.rank > 21:  
            self.rank -= 10
    # When called from game.py, this function the calculate_rank function.
    def get_rank(self):
        self.calculate_rank()
        return self.rank

    # This function prints players and the dealers 2nd card (hides the first).
    def display(self):
        if self.dealer:
            print("Hidden")
            print(self.cards[1])
        else:
            for card in self.cards:  
                print(card)
            print("rank:", self.get_rank())