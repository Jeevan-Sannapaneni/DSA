"""
Problem 019: Sort Colors

Difficulty: Medium

Problem Statement:
Given an array containing only 0s, 1s and 2s,
sort the array in-place.

Input:
N
Array

Output:
Sorted array

Time Complexity: O(N)
Space Complexity: O(1)
"""

n = int(input())
arr = list(map(int, input().split()))

low = 0
mid = 0
high = n - 1

while mid <= high:

    if arr[mid] == 0:
        arr[low], arr[mid] = arr[mid], arr[low]
        low += 1
        mid += 1

    elif arr[mid] == 1:
        mid += 1

    else:
        arr[mid], arr[high] = arr[high], arr[mid]
        high -= 1

print(*arr)
