# Documentation for `check_even_odd.py`


---

### Even or Odd

This program checks whether a given number is even or odd. It does this by asking the user to input a number, and then using an if statement to determine whether the number is divisible by 2 without a remainder (even) or has a remainder (odd).

Input Parameters:

* `num`: The number to be checked for evenness. This should be an integer.

Return Value:

* If the number is even, this function returns "The number is even." as a string.
* If the number is odd, this function returns "The number is odd." as a string.

Use Cases:

* To determine whether a given number is even or odd.
* To check if a number is divisible by 2 without a remainder.

Example Usage:
```python
# Ask the user for a number
num = int(input("Enter a number: "))

# Check if the number is even or odd
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
```
This program can be used to check whether a given number is even or odd. It does this by asking the user to input a number, and then using an if statement to determine whether the number is divisible by 2 without a remainder (even) or has a remainder (odd). The output of the program will be "The number is even" or "The number is odd", depending on whether the input number is even or odd.

