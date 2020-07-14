# Blackjack Poker
#### Code Louisville Python Project
#### Summer 2020


James Embry<br>
June 2020<br>
Tuesday Python Class <br>
Blackjack Poker Project <br>

This program follows examples found online and on Github:<br>
Title: Code Louisville Example<br>
Author: Zach Tibbitts<br>
Date: 2020<br>

Title: Tkinter GUI Programing by Example<br>
Author: David Love<br>
Date: 2018 <br>

# What is it? <br>
A program developed using Python that runs on the command line.  A player will play Blackjack Poker against the computer. 

# Technical Summary
* Python 3.8
* Visual Studio Code


# How to make the Project work.<br>
1. Open the GitHub link with Visual Studio Code.

2. Click on the *game.py* file tab.
2. Create a Console by Clicking  on Terminal and Open a New Terminal.
3. Run the program with VS Code using one of the following:
  * Ctrl F5
  * Click on the Run Python Icon (green triangle) at the top.
  * Click on Run on the top taskbar and select 'Run Without Debugging'.
4. Click in the *Console* and follow the prompts:
  * y for YES
  * n for NO
  * h for HIT
  * s for STAY

# Features<br>
* The Player is welcomed.
* A hand is delt for the Player and the Dealer.
* The Player's hand is shown with a total value.
* The Dealer's hand has 1 card hidden and 1 card shown with it's value (standard rules).
* The Player is asked if they want another card (Hit) or to stay with their current hand (Stick).
* A card is delt and the new value is displayed.
* The Player either loses or is asked to choose Hit or Stick.
* The winner is displayed.
* The Player is asked if they would like to continue to play or not.

# TEST ???????<br>
 
## Source Overview

This project consists of a 4 classes:

* `Game` The loop logic to run the game is contained in this class.
* `Card` This class instantiates a Card object.
    * It contains an `__init__` method to construct and initialize the card with a `suit` and `rank`(or point value).
    * It also contains a  `__repr__` method for proper formatting.
* `Deck` This class instantiates a Deck object.
    * When initialized with the `__init__` method, it creates an instance of a deck of 52 playing cards.
    * `shuffle()`: randomizes the order of the cards
    * `deal()`: removes the top card from the deck and returns it.
* `Hand` This class instantiates a Hand object.
    * When initialized with the `__init__` method, it creates an empty list object containing no cards and no point value.
    * `cards`: Is a list of `Card` objects in the hand.
    * `add_card(card)`: Is a method to put the given card into the hand.
    * `calculate_rank()`: Calculates the point value of a card. If the card is an ace, it has a point value of 11 or 1 if `self.rank` > 21.
    * `get_rank`: Is a method to calculate the total point value and returns it as `self.rank`.
    * `display()`: Is a method that prints the Dealer and Player hands to the console.

 


# Code Louisville requirements it meets.

This project fulfills the following requirements:

* Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program
    * There are two such loops. The outer (main) 'playing' loop and the inner 'Hit/Stick input' loop. Both are in `game.py`



* Create a class, then create at least one object of that class and populate it with data
    * All of `Card`, `Hand`, and `Deck` qualify.  See the classes for details.
* Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program
    * The `Hand` class creates a list of card objects for the player and the dealer.  The `Deck` class uses  list comprehension to create a list containing 52 cards and a shuffle method to randomize the list.

* Create and call at least 3 functions, at least one of which must return a value that is used.
    * The `deal()` function in the `Deck` class when called from `game.py` returns a `Card` from the top of the `Deck`.
    * The `add_card()` function in the `Hand` class is called from `game.py`, it appends a `Card` to the player or dealer `cards` list.
    * The `calculate_rank` function in the `Hand` class is called by the `get_rank` function. It calculates the value of the `card` in the `self.cards` list.


# `STOPPED HERE`********** WITH EDIT
* Create 3 or more unit tests for your application
    * They reside in `tests.py`
      

# Milestone List
Week 1: Outline project ideas. <br>
Week 3: Decide on a project and complete an outline <br>
Week 5: Build selection categories (card, deck, hand, and game.). <br>
Week 7: Check for problem and correct  mistakes. <br>
Week 10: Complete project. <br>
Week 12: Projects Due by Friday.



## Tests

Once your environment is set up, you can run tests with:

* `pipenv run python tests.py`
 

#### Additional Requirements
* Your code have comments that document major sections of your code to make it easier to read
    * Both inline comments and pydoc comments on the functions themselves
* Your project code is uploaded to your GitHub account, in its own repository, with at least 5 commits
* We need to see that you’ve used Git to update your GitHub profile at least 5 times
* It must include a README file located at the top level directory of your project that includes:
    * (You're reading it!)
    * A description of your project
    * What features you chose to included (so we know what to look for)
    * Any special instructions we might need to run your project
