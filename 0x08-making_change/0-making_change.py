#!/usr/bin/python3

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

    # Sort the coins in descending order
    coins.sort(reverse=True)

    # Initialize a variable to count the number of coins used
    count = 0

    # While the remaining amount is greater than 0
    while total > 0:
        # Find the largest coin that is less than or equal to the remaining amount
        for coin in coins:
            if coin <= total:
                break

        # Subtract the value of the coin from the remaining amount
        total -= coin

        # Increment the count of coins used
        count += 1

    # Return the count of coins used
    return count

