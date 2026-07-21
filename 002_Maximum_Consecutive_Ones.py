"""
Problem 002: Maximum Consecutive Ones

Difficulty: Easy

Problem Statement:
Given a binary array consisting of only 0s and 1s,
find the maximum number of consecutive 1s.

Input:
N
A1 A2 ... AN

Output:
Maximum consecutive 1s.

Example:
Input:
8
1 1 0 1 1 1 0 1

Output:
3

Time Complexity: O(N)
Space Complexity: O(1)
"""

n = int(input())
arr = list(map(int, input().split()))

count = 0
maximum = 0

for num in arr:
    if num == 1:
        count += 1
        maximum = max(maximum, count)
    else:
        count = 0

print(maximum)
