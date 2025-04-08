# Documentation for `Number_guessing.py`


Number Guessing Game
=====================

This is a simple game where the user has to guess a random number between 1 and 10. The game checks if the user's guess is equal to the secret number, and if it is, it prints out "You guessed it right!", otherwise it prints out "Oops! The correct number was [secret_number]."

The purpose of this program is to teach users about basic programming concepts such as variables, input/output, control structures (if-else), and functions. It also demonstrates how to generate random numbers using the `random` module in Python.

Use Cases
----------

1. Users can use this game to practice their guessing skills and learn about basic programming concepts.
2. Teachers can use this program as a teaching tool to help students understand the basics of programming, such as variables, input/output, control structures, and functions.
3. People who enjoy games can use this program to challenge themselves with different random numbers each time they play.

Input Parameters
---------------

The input parameters for this program are:

* `secret_number`: a random number between 1 and 10, generated using the `random.randint` function.
* `guess`: an integer entered by the user to guess the secret number.

Return Value
------------

If the user's guess is equal to the secret number, the program will print out "You guessed it right!", otherwise it will print out "Oops! The correct number was [secret_number]."

Format of Output
-----------------

The output of this program is a simple message that indicates whether the user has guessed the correct number or not. If the user's guess is equal to the secret number, the program will print out "You guessed it right!", otherwise it will print out "Oops! The correct number was [secret_number]."

Code Block
-----------

Here is the full code for this program:
```python
import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Ask the user to guess the number
guess = int(input("Guess a number between 1 and 10: "))

# Check the guess
if guess == secret_number:
    print("You guessed it right!")
else:
    print(f"Oops! The correct number was {secret_number}.")
```

