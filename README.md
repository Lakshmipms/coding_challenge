# This is a pairs sum counter program

This project provides a function `count_pairs_with_sum` that checks the number of pairs in an array of integers that 
sum up to a given value.

## Requirements

- Python 3.10

## Function Details

According to the given requirements
`count_pairs_with_sum(arr, X)`: Given a sorted list of integers `arr` and a target sum `X`, 
the function will return the number of pairs from the list that sum up to `X`. 
Each integer in the list can only be used in one pair.

## Running the Code

1. Ensure you have Python installed on your machine.
2. Navigate to the project directory.
3. You can import the function in your Python scripts using:
```python
from main import count_pairs_with_sum
```

## Testing the function

Tests for the count_pairs_with_sum function are provided in the iCode_Challenge.py file.
To run the tests:

1. Navigate to the project directory in the terminal or command prompt.
2. Execute the command: python -m unittest test_2iCodeChallenge.py

### Assumptions I have taken
I have used a two-pointer technique on a sorted array, making sure no number is used 
in more than one pair by adjusting both pointers when a matching pair is found.