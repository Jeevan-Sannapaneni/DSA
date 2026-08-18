

"""
Problem 073: Flood Fill

Difficulty: Easy

Problem Statement:
Given an image represented by a grid of integers,
starting from a given cell, change its color and all
connected cells having the same original color.

Cells are connected horizontally and vertically.

Input:
R C
Grid
Start row and column
New color

Output:
Modified grid.

Time Complexity: O(R * C)
Space Complexity: O(R * C)
"""

from collections import deque


rows, cols = map(int, input().split())

image = [
    list(map(int, input().split()))
    for _ in range(rows)
]

start_row, start_col = map(int, input().split())
new_color = int(input())

original_color = image[start_row][start_col]

if original_color != new_color:

    queue = deque([(start_row, start_col)])
    image[start_row][start_col] = new_color

    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    while queue:
        row, col = queue.popleft()

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and image[new_row][new_col] == original_color
            ):
                image[new_row][new_col] = new_color
                queue.append((new_row, new_col))


for row in image:
    print(*row)
