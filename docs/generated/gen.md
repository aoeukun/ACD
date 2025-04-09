# Documentation for `gen.py`


Here is the generated documentation for the above Python code:

### `main`

The `main` function is the entry point of the program. It prompts the user to enter a string and prints its reversal.

**Args:**

* `text (str)`: The input text.

**Returns:**

* `None`: This function does not return any value.

**Raises:**

* `ValueError`: If the input is not a string.

**Example:**
```python
if __name__ == "__main__":
    main()
```

### `input`

The `input` function reads a line from standard input and returns it as a string.

**Args:**

* `prompt (str, optional)`: The prompt to display before reading input. If not specified, the prompt is empty.

**Returns:**

* `line (str)`: The input text read from standard input.

**Raises:**

* `EOFError`: If the user hits End of File while reading input.

**Example:**
```python
input("Enter a string: ")
```

### `print`

The `print` function prints its arguments to standard output, followed by a newline character.

**Args:**

* `text (str)`: The text to print.

**Returns:**

* `None`: This function does not return any value.

**Raises:**

* `TypeError`: If the argument is not a string or bytes.

**Example:**
```python
print("Reversed:", text[::-1])
```

