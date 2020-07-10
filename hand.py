class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.rank = 0

    def add_card(self, card):
        self.cards.append(card)
       
    def calculate_rank(self):
        self.rank = 0
        has_ace = False
        for card in self.cards:
            if card.rank.isnumeric():
                self.rank += int(card.rank)
            else:
                if card.rank == "A":
                    has_ace = True
                    self.rank += 11
                else:
                    self.rank += 10

        if has_ace and self.rank > 21:   # If over 21 Ace rank drops from 11 to 1
            self.rank -= 10

    def get_rank(self):
        self.calculate_rank()
        return self.rank


    def display(self):
        if self.dealer:
            print("hidden")
            print(self.cards[1])
        else:
            for card in self.cards:  
                print(card)
            print("rank:", self.get_rank())