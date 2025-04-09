# Documentation for `Number_guessing.py`

Here are the generated docstrings for each function and class in the code:
```python
# Number guessing game

import random

# Generate a random number between 1 and 10
def generate_random_number():
    """
    Generates a random number between 1 and 10.
    
    Returns:
        int: The generated random number.
    """
    return random.randint(1, 10)

# Ask the user to guess the number
def ask_user_to_guess():
    """
    Asks the user to guess a number between 1 and 10.
    
    Returns:
        int: The guessed number.
    """
    return int(input("Guess a number between 1 and 10: "))

# Check the guess
def check_guess(secret_number, guess):
    """
    Checks if the guess is correct or not.
    
    Args:
        secret_number (int): The random number generated.
        guess (int): The user's guess.
    
    Returns:
        bool: True if the guess is correct, False otherwise.
    """
    return guess == secret_number

# Print the result of the guess
def print_result(correct, secret_number):
    """
    Prints the result of the guess.
    
    Args:
        correct (bool): True if the guess is correct, False otherwise.
        secret_number (int): The random number generated.
    """
    if correct:
        print("You guessed it right!")
    else:
        print(f"Oops! The correct number was {secret_number}.")

# Main function
def main():
    """
    Main function of the program.
    
    Returns:
        None
    """
    secret_number = generate_random_number()
    guess = ask_user_to_guess()
    correct = check_guess(secret_number, guess)
    print_result(correct, secret_number)

if __name__ == "__main__":
    main()
```

