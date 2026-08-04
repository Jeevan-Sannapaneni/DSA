"""
Problem 033: Binary Search

Difficulty: Easy

Problem Statement:
Given a sorted array of integers and a target value,
find the index of the target.
If the target is not present, print -1.

Input:
N
Sorted Array
Target

Output:
Index of target or -1.

Time Complexity: O(log N)
Space Complexity: O(1)
"""

n = int(input())
arr = list(map(int, input().split()))
target = int(input())

left = 0
right = n - 1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
        print(mid)
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print(-1)
