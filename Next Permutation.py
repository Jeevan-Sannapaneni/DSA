"""
Problem 020: Next Permutation

Difficulty: Medium

Problem Statement:
Given an array representing a permutation,
find the next lexicographically greater permutation.
If it does not exist, return the smallest permutation.

Input:
N
Array

Output:
Next permutation

Time Complexity: O(N)
Space Complexity: O(1)
"""

n = int(input())
arr = list(map(int, input().split()))

i = n - 2

while i >= 0 and arr[i] >= arr[i + 1]:
    i -= 1

if i >= 0:
    j = n - 1
    while arr[j] <= arr[i]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]

left = i + 1
right = n - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(*arr)
