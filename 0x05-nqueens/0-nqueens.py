#!/usr/bin/python3
"""The N queens puzzle is the challenge of placing N non-attacking queens
on an NxN chessboard. Write a program that solves the N queens problem.
"""
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    n = argv[1]
    if n.isnumeric():
        n = int(n)
    else:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)

    cols = set()
    posDia = set()  # (r + c)
    negDia = set()  # (r - c)

    results = []
    res = []

    def backtrack(r):
        """function"""
        if r == n:
            results.append(res.copy())
            return

        for c in range(n):
            if c in cols or (c + r) in posDia or (r - c) in negDia:
                continue

            cols.add(c)
            posDia.add(c + r)
            negDia.add(r - c)
            res.append([r, c])

            backtrack(r + 1)

            cols.remove(c)
            posDia.remove(c + r)
            negDia.remove(r - c)
            res.remove([r, c])

    backtrack(0)

    for one in results:
        print(one)
