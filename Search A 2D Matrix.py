"""
Problem 032: Search A 2D Matrix

Difficulty: Medium

Problem Statement:
Given an M x N matrix where each row is sorted
and the first element of each row is greater than
the last element of the previous row,
determine whether a target value exists.

Input:
Rows Columns
Matrix
Target

Output:
YES if found, otherwise NO

Time Complexity: O(log(M×N))
Space Complexity: O(1)
"""

rows, cols = map(int, input().split())

matrix = []

for _ in range(rows):
    matrix.append(list(map(int, input().split())))

target = int(input())

left = 0
right = rows * cols - 1

found = False

while left <= right:

    mid = (left + right) // 2

    value = matrix[mid // cols][mid % cols]

    if value == target:
        found = True
        break
    elif value < target:
        left = mid + 1
    else:
        right = mid - 1

if found:
    print("YES")
else:
    print("NO")
