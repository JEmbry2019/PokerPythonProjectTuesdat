Blackjack Poker
Code Louisville Python Project
Summer 2020

James Embry
READ ME
 SAmple Read Me


James Embry <br>
March 2020 <br>
Tuesday Project Class <br>
Camp Registration Project <br>

What is it? <br>
A program developed using C# that allows camp coordinators to enter and save camper registration information.  Using EntityFramwork , the application will create a user interface to convert the user input data into an object of a specific class and store it in a database.

Technical Summary <br>
C# <br>
Visual Studio Code <br>
.NET SDK  3.1.102 <br>
Microsoft EntityFramework Core <br>
Microsoft EntityFramework SQL Server (Database) <br>
Microsoft EntityFramework dotnet CLI <br>
Microsoft EntityFramework dotnet Design <br>
HTML, CSS, or JavaScript <br>
Json <br>
MVC/Razor <br>

How to make the Project work.<br>
1 Open the GitHub link with Visual Studio Code.<br>
2 Create a Console by Clicking  on Terminal and Open a New Terminal.<br>
3 In the Console type dotnet ef database update then press ENTER.<br>
4 In the Console type dotnet run then press ENTER.<br>
The program will build and create a local web address and other directions in the console.<br>
5 Type the address (http://localhost5001) into a Chrome browser.<br>
6 Click on Campers:<br>
  Click on Create New.<br>
    Follow the prompts to enter a camper.<br>
  Click on Create.<br>
7 Click on Games:<br>
  Click on Create New.<br>
    Follow the prompts to select your 3 games.<br>
  Click on Create.<br>
8 Click on Meals:<br>
  Click on Create New:<br>
    Follow the prompts to select your 3 meals.<br>
  Click on Create.<br>    
9 Click on Enrollments:<br>
  Click on Create New:<br> 
  Follow the prompts to enroll your camper.<br>
  Select your name, meals, games, and grade level.<br>
  Click on Create.<br>


Features Include:<br>
Homepage<br>
Privacy page example<br>
Camper page (first and last name, email, phone, enrollment date, (Create, Edit, Details, and Delete))<br>
Game Choice page (3 dropdown lists with 3 chioces of games in each (Create, Edit, Details, and Delete))<br>
Meal Choice page (3 dropdown lists with 3 chioces of food in each (Create, Edit, Details, and Delete))<br>
Enrollment page (Lists all campers with details) (Enroll new campers on Create page with dropdown lists that inclide the campers full name, school level (Primary, Middle, or High), their game selection (and other choices),  thier food selection (and other choices), (Create, Edit, Details, and Delete))<br>

Milestone List <br>
Week 1: Outline Project. <br>
Week 3: Add and retrieve data (Name) to a json file or database. <br>
Week 5: Build selection categories (age, food choice, etc.). <br>
Week 7: Create a user-friendly interface. <br>
Week 8: Complete project. <br>



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
