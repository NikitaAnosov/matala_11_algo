# Fractional Decomposition Solver

Python implementation for solving the fractional budget decomposition problem (Question 3).

## Requirements

* Python 3.x
* `networkx` library

## Installation

Install the required library:

```bash
pip install networkx
```

## Usage

The main script is `fractional.py`. To run the solver and see predefined test cases:

```bash
python fractional.py
```

You can also import the function in your own code:

```python
from fractional import find_decomposition

budget = [400, 50, 50, 0]
preferences = [
    {0, 1},  # Citizen 0 supports issues 0 and 1
    {0, 2},  # Citizen 1 supports issues 0 and 2
    {0, 3},  # Citizen 2 supports issues 0 and 3
    {1, 2},  # Citizen 3 supports issues 1 and 2
    {0}      # Citizen 4 supports issue 0 only
]

decomp = find_decomposition(budget, preferences)
if decomp is None:
    print("The budget is not decomposable.")
else:
    print("Decomposition matrix:")
    for i, row in enumerate(decomp):
        print(i, row)
```

## Test Cases

The script includes several test scenarios:

* Trivial single issue
* All zero budget
* Simple decomposable
* Non-decomposable
* Unequal preferences
* Zero-preference citizen
* Question 3 example

Add or modify test cases in the `test_cases` list at the bottom of `fractional.py`.

## Credits

chatGPT = [Link](https://chatgpt.com/share/6847217a-2960-800b-a71c-904f5c04f8a6)
