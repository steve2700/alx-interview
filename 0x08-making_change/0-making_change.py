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

    # Initialize an array to store the minimum number of coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
