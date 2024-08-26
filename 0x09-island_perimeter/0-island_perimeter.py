#!/usr/bin/python3
"""Interview Problem Graph"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    if not grid:
        return 0

    perimeter = [0]
    n = 0
    q = []
    seen = set()

    def countZeros(row, col):
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        count = 0

        for one in directions:
            r = row + one[0]
            c = col + one[1]
            if (r not in range(0, len(grid)) or
                    c not in range(0, len(grid[0])) or
                    grid[r][c] == 0):
                count += 1

        return count

    def DFS(row_root, col_root):
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        while q:
            row, col = q.pop()

            for one in directions:
                r = row + one[0]
                c = col + one[1]

                if r in range(0, len(grid)) and c in range(0, len(grid[0])):
                    if grid[r][c] == 1:
                        if (r, c) not in seen:
                            seen.add((r, c))
                            q.append((r, c))
                            perimeter[0] += countZeros(r, c)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1 and (row, col) not in seen:
                q.append((row, col))
                seen.add((row, col))
                perimeter[0] += countZeros(row, col)
                DFS(row, col)

    return perimeter[0]
