"""
Problem 004: Second Largest Element

Difficulty: Easy

Problem Statement:
Given an array of integers, find the second largest distinct
element. If it doesn't exist, print -1.

Input:
N
A1 A2 ... AN

Output:
Second largest element.

Time Complexity: O(N)
Space Complexity: O(1)
"""

n = int(input())
arr = list(map(int, input().split()))

first = second = float('-inf')

for num in arr:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num

if second == float('-inf'):
    print(-1)
else:
    print(second)
