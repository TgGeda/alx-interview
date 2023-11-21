#!/usr/bin/python3
"""Change making module.
"""

from typing import List

def makeChange(coins: List[int], total: int) -> int:
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.

    Args:
    coins (List[int]): A list of coin denominations.
    total (int): The total amount for which change needs to be made.

    Returns:
    int: The fewest number of coins needed to meet the total amount.
    """
    if total <= 0:
        return 0

    remaining_amount = total
    coins_count = 0
    coin_index = 0
    sorted_coins = sorted(coins, reverse=True)
    num_coins = len(coins)

    while remaining_amount > 0:
        if coin_index >= num_coins:
            return -1
        if remaining_amount - sorted_coins[coin_index] >= 0:
            remaining_amount -= sorted_coins[coin_index]
            coins_count += 1
        else:
            coin_index += 1

    return coins_count

