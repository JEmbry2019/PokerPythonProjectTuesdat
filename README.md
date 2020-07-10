# Blackjack Poker
#### Code Louisville Python Project
#### Summer 2020


James Embry <br>
June 2020 <br>
Tuesday Python Class <br>
Blackjack Poker Project <br>
This program follows examples found online and on Github:
* Title: Code Louisville Example
* Author: Zach Tibbitts
* Date: 2020

* Title: Tkinter GUI Programing by Example
* Author: David Love
* Date: 2018 

# What is it? <br>
A program developed using Python that runs on the command line.  A player will play Blackjack Poker against the computer. 

# Technical Summary <br>
* Python 3.8 <br>
* Visual Studio Code <br>


# How to make the Project work.<br>
1. Open the GitHub link with Visual Studio Code.<br>
2. Click on the *game.py* file tab.
2. Create a Console by Clicking  on Terminal and Open a New Terminal.
3. Run the program with VS Code using one of the following:
  * Ctrl F5
  * Click on the Run Python Icon (green triangle) at the top.
  * Click on Run on the top taskbar and select 'Run Without Debugging'.


# TEST ???????<br>
 
## Source Overview

This project consists of a few classes:

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

      ***** STOPPED HERE  *****  With Edit.
    
The game loop logic itself is contained in the `Game` class. Check the comments in that file for more information





### Requirements:

This project fulfills the following requirements:

* Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program
    * There are two such loops. The outer "Play again" one and the inner "hit/stay" loop. Both are in `game.py`
* Create a class, then create at least one object of that class and populate it with data
    * All of `Card`, `Hand`, and `Deck` qualify
* Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program
    * Both `Hand` and `Deck` use a list internally to store their data
* Create and call at least 3 functions, at least one of which must return a value that is used
    * So many functions. In particular `draw()` returns a value, a `Card` that is used
* Create 3 or more unit tests for your application
    * They reside in `tests.py`

SAMPLE BELOW ------------- SAMPLE BELOW
Features Include:<br>
Homepage<br>
Privacy page example<br>
Camper page (first and last name, email, phone, enrollment date, (Create, Edit, Details, and Delete))<br>
Game Choice page (3 dropdown lists with 3 chioces of games in each (Create, Edit, Details, and Delete))<br>
Meal Choice page (3 dropdown lists with 3 chioces of food in each (Create, Edit, Details, and Delete))<br>
Enrollment page (Lists all campers with details) (Enroll new campers on Create page with dropdown lists that inclide the campers full name, school level (Primary, Middle, or High), their game selection (and other choices),  thier food selection (and other choices), (Create, Edit, Details, and Delete))<br> -->

Milestone List <br>
Week 1: Outline project ideas. <br>
Week 3: Decide on a project and complete an outline <br>
Week 5: Build selection categories (cards, deck, player, scoring, CSV file.). <br>
Week 7: Check for problem and correct  mistakes. <br>
Week 10: Complete project. <br>
Week 12: Projects Due by Friday.



 # Blackjack

#### Sample CodeLouisville Project

A simple command line Blackjack game

## Installation & Running

This project uses `Pipenv` to run.

* Check out the source code locally
* Inside the project dir, run `pipenv install`
* Run `pipenv run python game.py`

## Tests

Once your environment is set up, you can run tests with:

* `pipenv run python tests.py`
 
## Source Overview

This project consists of a few classes:

* `Card` is a simple datastructure containing a `rank` and `suit` value
    * It contains an `is_facecard()` method to check if it is a face card
* `Hand` is a class with the following properties:
    * `cards`: A list of `Card` objects in the hand
    * `add_card(card)`: A method to put the given card into the hand
    * `score()`: computes the Blackjack score for the hand
    * `is_bust()`: returns True if the score is over 21
* `Deck` is a class representing the yet-undrawn cards in the Deck.
    * It is initialized as a standard deck of 52 playing cards
    * `shuffle()`: randomizes the order of the cards
    * `draw()`: removes the top card from the deck and returns it.
    
The game loop logic itself is contained in the `Game` class. Check the comments in that file for more information

### Requirements:

This project fulfills the following requirements:

* Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program
    * There are two such loops. The outer "Play again" one and the inner "hit/stay" loop. Both are in `game.py`
* Create a class, then create at least one object of that class and populate it with data
    * All of `Card`, `Hand`, and `Deck` qualify
* Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program
    * Both `Hand` and `Deck` use a list internally to store their data
* Create and call at least 3 functions, at least one of which must return a value that is used
    * So many functions. In particular `draw()` returns a value, a `Card` that is used
* Create 3 or more unit tests for your application
    * They reside in `tests.py`

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
