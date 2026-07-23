"""
Problem 003: Move Zeros To End

Difficulty: Easy

Problem Statement:
Given an array of integers, move all zeros to the end while
maintaining the relative order of non-zero elements.

Input:
N
A1 A2 ... AN

Output:
Modified array.

Time Complexity: O(N)
Space Complexity: O(1)
"""

n = int(input())
arr = list(map(int, input().split()))

pos = 0

for i in range(n):
    if arr[i] != 0:
        arr[pos], arr[i] = arr[i], arr[pos]
        pos += 1

print(*arr)
