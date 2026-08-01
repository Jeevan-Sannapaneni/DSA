"""
Problem 018: Find All Duplicates In Array

Difficulty: Medium

Problem Statement:
Given an integer array, print all elements that appear
more than once in ascending order.
If there are no duplicates, print -1.

Input:
N
Array

Output:
Duplicate elements

Time Complexity: O(N)
Space Complexity: O(N)
"""

n = int(input())
arr = list(map(int, input().split()))

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

duplicates = []

for key in sorted(freq):
    if freq[key] > 1:
        duplicates.append(key)

if duplicates:
    print(*duplicates)
else:
    print(-1)
