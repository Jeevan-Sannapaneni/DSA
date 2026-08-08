"""
Problem 044: Largest Rectangle in Histogram

Difficulty: Hard

Problem Statement:
Given an array representing the heights of histogram bars,
find the largest rectangular area that can be formed.

Each bar has width 1.

Input:
N
Heights

Output:
Largest rectangle area.

Time Complexity: O(N)
Space Complexity: O(N)
"""

n = int(input())
heights = list(map(int, input().split()))

stack = []
maximum_area = 0

for i in range(n + 1):

    current_height = 0 if i == n else heights[i]

    while stack and heights[stack[-1]] > current_height:

        height = heights[stack.pop()]

        if stack:
            width = i - stack[-1] - 1
        else:
            width = i

        maximum_area = max(maximum_area, height * width)

    stack.append(i)

print(maximum_area)
