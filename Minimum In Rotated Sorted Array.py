"""
Problem 036: Find Minimum In Rotated Sorted Array

Difficulty: Medium

Problem Statement:
Given a rotated sorted array of distinct integers,
find the minimum element.

Input:
N
Array

Output:
Minimum element

Time Complexity: O(log N)
Space Complexity: O(1)
"""

n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1

while left < right:
    mid = (left + right) // 2

    if arr[mid] > arr[right]:
        left = mid + 1
    else:
        right = mid

print(arr[left])
