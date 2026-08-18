

"""
Problem 072: Number of Islands

Difficulty: Medium

Problem Statement:
Given a grid containing '1' for land and '0' for water,
find the number of separate islands.

An island is formed by connecting adjacent land cells
horizontally or vertically.

Input:
R C
R rows containing 0 and 1

Output:
Number of islands.

Time Complexity: O(R * C)
Space Complexity: O(R * C)
"""

from collections import deque


rows, cols = map(int, input().split())

grid = [list(input().strip()) for _ in range(rows)]

islands = 0

directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]


def bfs(start_row, start_col):
    queue = deque([(start_row, start_col)])
    grid[start_row][start_col] = '0'

    while queue:
        row, col = queue.popleft()

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and grid[new_row][new_col] == '1'
            ):
                grid[new_row][new_col] = '0'
                queue.append((new_row, new_col))


for i in range(rows):
    for j in range(cols):

        if grid[i][j] == '1':
            islands += 1
            bfs(i, j)

print(islands)
