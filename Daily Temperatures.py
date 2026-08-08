"""
Problem 042: Daily Temperatures

Difficulty: Medium

Problem Statement:
Given an array of daily temperatures, find how many days
you have to wait until a warmer temperature for each day.

If there is no future warmer day, output 0.

Input:
N
Temperatures

Output:
Number of days to wait for a warmer temperature.

Time Complexity: O(N)
Space Complexity: O(N)
"""

n = int(input())
temperatures = list(map(int, input().split()))

answer = [0] * n
stack = []

for i in range(n - 1, -1, -1):

    while stack and temperatures[stack[-1]] <= temperatures[i]:
        stack.pop()

    if stack:
        answer[i] = stack[-1] - i

    stack.append(i)

print(*answer)
