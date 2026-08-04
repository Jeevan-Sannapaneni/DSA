"""
Problem 034: First And Last Position

Difficulty: Medium

Problem Statement:
Given a sorted array and a target,
find the first and last occurrence of the target.

If the target is not found, print -1 -1.

Input:
N
Sorted Array
Target

Output:
First and last index.

Time Complexity: O(log N)
Space Complexity: O(1)
"""

n = int(input())
arr = list(map(int, input().split()))
target = int(input())

first = -1
last = -1

left = 0
right = n - 1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] >= target:
        right = mid - 1
    else:
        left = mid + 1

    if arr[mid] == target:
        first = mid

left = 0
right = n - 1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] <= target:
        left = mid + 1
    else:
        right = mid - 1

    if arr[mid] == target:
        last = mid

print(first, last)
