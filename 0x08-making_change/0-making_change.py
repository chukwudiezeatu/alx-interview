#!/usr/bin/python3
"""Coin Problem"""


def makeChange(coins, total):
    """return the fewest number of coins needed to meet a given amount"""
    if total <= 0:
        return 0

    coins = sorted(coins, reverse=True)

    count = 0
    for coin in coins:
        if total == 0:
            break
        count += total // coin
        total = total % coin

    if total != 0:
        return -1

    return count
