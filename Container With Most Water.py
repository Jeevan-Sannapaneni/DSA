"""
Problem 028: Container With Most Water

Difficulty: Medium

Problem Statement:
Given an array where each element represents the height
of a vertical line, find two lines that together with
the x-axis form a container containing the maximum water.

Input:
N
Heights

Output:
Maximum area

Time Complexity: O(N)
Space Complexity: O(1)
"""

n = int(input())
height = list(map(int, input().split()))

left = 0
right = n - 1

maximum = 0

while left < right:

    area = min(height[left], height[right]) * (right - left)

    maximum = max(maximum, area)

    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

print(maximum)
