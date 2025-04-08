# Documentation for `three.py`


# Even or Odd

A simple program to check whether a given number is even or odd.

## Functions

### `main()`

This function is the entry point of the program. It asks the user for a number and checks if it's even or odd using the `is_even()` function.

```python
def main():
    num = int(input("Enter a number: "))
    if is_even(num):
        print("The number is even.")
    else:
        print("The number is odd.")
```

### `is_even()`

This function checks whether a given number is even or not. It takes an integer as input and returns a boolean value indicating if the number is even.

```python
def is_even(n):
    return n % 2 == 0
```

## Usage

To use this program, follow these steps:

1. Save the code in a file with a `.py` extension (e.g., `even_or_odd.py`).
2. Open a terminal or command prompt and navigate to the directory where the file is saved.
3. Run the program by typing `python even_or_odd.py` and pressing Enter.
4. The program will ask you for a number, enter a number and press Enter.
5. The program will output whether the number is even or odd.

## Inputs

* `num`: An integer input by the user.

## Outputs

* If the number is even: "The number is even."
* If the number is odd: "The number is odd."

## Return types

* Boolean value indicating whether the number is even or not.

