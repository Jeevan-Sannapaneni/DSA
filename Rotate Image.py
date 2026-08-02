"""
Problem 031: Rotate Image

Difficulty: Medium

Problem Statement:
Given an N x N matrix, rotate it by 90 degrees
clockwise in-place.

Input:
N
Matrix

Output:
Rotated Matrix

Time Complexity: O(N²)
Space Complexity: O(1)
"""

n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

# Transpose
for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Reverse each row
for i in range(n):
    matrix[i].reverse()

for row in matrix:
    print(*row)
