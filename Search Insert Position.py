"""
Problem 037: Search Insert Position

Difficulty: Easy

Problem Statement:
Given a sorted array and a target,
return its index if found.
Otherwise, return the index where it should be inserted.

Input:
N
Sorted Array
Target

Output:
Insert position

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
    print(left)
