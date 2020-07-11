import random

from card import Card
from deck import Deck
from hand import Hand



class Game:
    def __init__(self):
    #     pass

    # def play(self):

        # This is the start of the outer loop (main loop) where the player decides to play again or exit the game.
        playing = True
        
        while playing:
            # This calls the Deck class and creates a shuffled deck.
            self.deck = Deck()
            self.deck.shuffle()
            # This call the Hand class and 2 Hand instances.
            self.player_hand = Hand()
            self.dealer_hand = Hand(dealer=True)
            # This code deals 2 cards to player and dealer and displays results.
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
            # This loop is an inner loop that has nested loops within it.
            # We stay in this loop until a winner is decided.
            while not game_over:
                # If the player or dealer has blackjack 'continue' allows us to exit the loop.
                player_has_blackjack, dealer_has_blackjack = self.check_for_blackjack()
                if player_has_blackjack or dealer_has_blackjack:
                    game_over = True
                    self.show_blackjack_results(player_has_blackjack, dealer_has_blackjack)
                    continue
                # This nested loop allows the player to select a card (or stay), and determins the winner.                
                choice = input("Please choose [Hit / Stick] ").lower()
                while choice not in ["h", "s", "hit", "stick"]:
                    choice = input("Please enter 'hit' or 'stick' (or H/S) ").lower()
                # If hit is selected, add_card function in the Hand class is called to add a card and player_is_over checks for > 21 (bust).
                if choice in ['hit', 'h']:
                    self.player_hand.add_card(self.deck.deal())
                    self.player_hand.display()
                    if self.player_is_over():
                        print("You have lost!")
                        game_over = True
                else:
                # This code displays the cards and determines the winner and exits the loop.    
                    player_hand_rank = self.player_hand.get_rank()
                    dealer_hand_rank = self.dealer_hand.get_rank()

                    print("Final Results")
                    print("Your hand:", player_hand_rank)
                    print("Dealer's hand:", dealer_hand_rank)

                    if player_hand_rank > dealer_hand_rank:
                        print("You Win!")
                    elif player_hand_rank == dealer_hand_rank:
                        print("Tie!")
                    else:
                        print("Dealer Wins!")
                    game_over = True
        # The player decides to play again the main loop repeats or not to play and the loop exits the outer (main) loop
            again = input("Play Again? [Y/N] ")
            while again.lower() not in ["y", "n"]:
                again = input("Please enter Y or N ")
            if again.lower() == "n":
                print("Thanks for playing!")
                playing = False
            else:
                game_over = False
    # This method checks to see if the player's hand is > 21 (bust).
    def player_is_over(self):
        return self.player_hand.get_rank() > 21

    # This method checks to see if the player or dealer has exactly 21 (Blackjack).
    def check_for_blackjack(self):
        player = False
        dealer = False
        if self.player_hand.get_rank() == 21:
            player = True
        if self.dealer_hand.get_rank() == 21:
            dealer = True

        return player, dealer
    # This method checks for Blackjack and prints the winner.
    def show_blackjack_results(self, player_has_blackjack, dealer_has_blackjack):
        if player_has_blackjack and dealer_has_blackjack:
            print("Both players have blackjack! Draw!")

        elif player_has_blackjack:
            print("You have blackjack! You win!")

        elif dealer_has_blackjack:
            print("Dealer has blackjack! Dealer wins!")


if __name__ == "__main__":
    g = Game()
    # g.play()

    