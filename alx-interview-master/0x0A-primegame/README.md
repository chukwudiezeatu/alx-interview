# 0x0A. Prime Game

## Algorithm | Python

**Project Duration**: June 14, 2024, 6:00 AM - June 21, 2024, 6:00 AM  
**Checker Release**: June 16, 2024, 12:00 AM  
**Auto Review**: At the deadline

## Overview
For this project, you will need to leverage your understanding of prime numbers, game theory, and algorithm optimization to solve a competitive game scenario. The challenge involves determining the winner of a game based on the strategic removal of prime numbers and their multiples from a set of consecutive integers.

## Concepts Needed
### Prime Numbers
- Understanding what prime numbers are.
- Efficient algorithms for identifying prime numbers within a range.

### Sieve of Eratosthenes
- An efficient algorithm for finding all prime numbers up to any given limit, which can be particularly useful for this task.

### Game Theory
- Basic principles of competitive games where players take turns and the concept of optimal play.
- Understanding win conditions and strategies that lead to a win or loss.

### Dynamic Programming/Memoization
- Using previous results to make future calculations faster, potentially necessary for optimizing the solution for multiple rounds of the game.

### Python Programming
- Loops and conditional statements for implementing game logic and algorithms.
- Arrays and lists for storing the integers and tracking removed numbers.

## Resources
### Prime Numbers and Sieve of Eratosthenes
- [Khan Academy: Prime Numbers](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:chapter-1-core-content/prime-numbers/v/prime-numbers)
- [Sieve of Eratosthenes in Python](https://www.geeksforgeeks.org/sieve-of-eratosthenes/)

### Game Theory Basics
- [Game Theory Introduction](https://www.khanacademy.org/economics-finance-domain/microeconomics/nash-equilibrium-tutorial)

### Dynamic Programming
- [What Is Dynamic Programming With Python Examples](https://www.geeksforgeeks.org/dynamic-programming/)

### Python Official Documentation
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)

## Additional Resources
- Mock Technical Interview

## Requirements
- **General**
  - Allowed editors: `vi`, `vim`, `emacs`
  - All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
  - All your files should end with a new line
  - The first line of all your files should be exactly `#!/usr/bin/python3`
  - A `README.md` file, at the root of the folder of the project, is mandatory
  - Your code should use the PEP 8 style (version 1.7.x)
  - All your files must be executable

## Tasks
### 0. Prime Game
**Mandatory**

Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including `n`, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play `x` rounds of the game, where `n` may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

**Prototype:**
```python
def isWinner(x, nums)

