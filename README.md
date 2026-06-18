# String Utils Library

## Project Description

This project is a simple Python string utility library.

It includes three functions:

1. **reverse_words(s)**

   * Reverses the order of words in a string.
   * Example:

     ```
     "hello world" -> "world hello"
     ```

2. **count_vowels(s)**

   * Counts the number of vowels (a, e, i, o, u) in a string.
   * Example:

     ```
     "hello" -> 2
     ```

3. **is_palindrome(s)**

   * Checks whether a string is a palindrome.
   * Example:

     ```
     "level" -> True
     "hello" -> False
     ```

---

## Files

```
string_utils.py
test_string_utils.py
README.md
```

* `string_utils.py` contains the utility functions.
* `test_string_utils.py` contains pytest test cases.
* `README.md` contains project documentation.

---

## Requirements

* Python 3.x
* pytest

Install pytest:

```bash
pip install pytest
```

---

## How to Run

You can import the functions into another Python file:

```python
from string_utils import reverse_words
from string_utils import count_vowels
from string_utils import is_palindrome

print(reverse_words("hello world"))
print(count_vowels("hello"))
print(is_palindrome("level"))
```

Run the file:

```bash
python string_utils.py
```

---

## How to Run Tests

Run all tests with:

```bash
pytest
```

or

```bash
pytest test_string_utils.py
```

Expected result:

```text
=================
9 passed
=================
```

---

## Test Coverage

Each function includes:

* Normal test cases
* Edge cases
* Invalid input test cases

This helps ensure the functions work correctly under different conditions.
