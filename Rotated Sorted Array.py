"""
Problem 035: Search In Rotated Sorted Array

Difficulty: Medium

Problem Statement:
Given a rotated sorted array of distinct integers
and a target value, return its index.
If it is not present, print -1.

Input:
N
Array
Target

Output:
Index of target.

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

    if arr[left] <= arr[mid]:

        if arr[left] <= target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    else:

        if arr[mid] < target <= arr[right]:
            left = mid + 1
        else:
            right = mid - 1

else:
    print(-1)
