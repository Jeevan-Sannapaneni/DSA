"""
Problem 005: Check Array Sorted

Difficulty: Easy

Problem Statement:
Given an array of integers, determine whether it is sorted in
non-decreasing order.

Input:
N
A1 A2 ... AN

Output:
YES if sorted, otherwise NO.

Time Complexity: O(N)
Space Complexity: O(1)
"""

n = int(input())
arr = list(map(int, input().split()))

sorted_array = True

for i in range(n - 1):
    if arr[i] > arr[i + 1]:
        sorted_array = False
        break

if sorted_array:
    print("YES")
else:
    print("NO")
