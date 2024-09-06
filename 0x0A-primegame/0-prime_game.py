#!/usr/bin/python3
"""Prime Game"""


def genprimes(n):
    """Generates prime numbers up to n"""
    primes = [True for i in range(n + 1)]

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    return primes


def isWinner(x, nums):
    """Determines the winner of the game"""
    maria = 0
    ben = 0
    primes = genprimes(max(nums))

    if x != len(nums):
        return None

    for i in nums:
        flag = True  # Maria's turn
        copy = primes[:i + 1]
        selected = [False for _ in range(i + 1)]

        for p in range(2, len(copy)):
            if copy[p]:
                for j in range(p, len(copy), p):
                    selected[j] = True
                flag = not flag

        if not flag:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
