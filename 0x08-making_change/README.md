# Coin Change Calculator

## Overview

This Python script provides a function, `makeChange`, to determine the fewest number of coins needed to meet a given amount total. The solution follows a simple greedy algorithm.

## Function Signature

```python
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
    - coins (list): A list of coin values.
    - total (int): The target total amount.

    Returns:
    - int: Fewest number of coins needed to meet the total.
           If total is 0 or less, return 0.
           If total cannot be met by any number of coins you have, return -1.
    """

