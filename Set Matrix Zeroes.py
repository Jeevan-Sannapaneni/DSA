"""
Problem 030: Set Matrix Zeroes

Difficulty: Medium

Problem Statement:
Given an M x N matrix, if an element is 0, set its
entire row and column to 0.

Input:
Rows Columns
Matrix

Output:
Modified Matrix

Time Complexity: O(M×N)
Space Complexity: O(M+N)
"""

rows, cols = map(int, input().split())

matrix = []

for _ in range(rows):
    matrix.append(list(map(int, input().split())))

zero_rows = set()
zero_cols = set()

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 0:
            zero_rows.add(i)
            zero_cols.add(j)

for i in range(rows):
    for j in range(cols):
        if i in zero_rows or j in zero_cols:
            matrix[i][j] = 0

for row in matrix:
    print(*row)
