"""
Problem 027: Trapping Rain Water

Difficulty: Hard

Problem Statement:
Given an array representing the elevation map where
the width of each bar is 1, compute how much water
can be trapped after raining.

Input:
N
Heights

Output:
Total trapped water

Time Complexity: O(N)
Space Complexity: O(1)
"""

n = int(input())
height = list(map(int, input().split()))

left = 0
right = n - 1

left_max = 0
right_max = 0

water = 0

while left <= right:

    if height[left] <= height[right]:

        if height[left] >= left_max:
            left_max = height[left]
        else:
            water += left_max - height[left]

        left += 1

    else:

        if height[right] >= right_max:
            right_max = height[right]
        else:
            water += right_max - height[right]

        right -= 1

print(water)
