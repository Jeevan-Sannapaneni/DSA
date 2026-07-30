"""
Problem 024: Longest Consecutive Sequence

Difficulty: Medium

Problem Statement:
Given an unsorted array of integers, find the length
of the longest consecutive elements sequence.

Input:
N
Array

Output:
Length of the longest consecutive sequence.

Time Complexity: O(N)
Space Complexity: O(N)
"""

n = int(input())
arr = list(map(int, input().split()))

nums = set(arr)
longest = 0

for num in nums:
    if num - 1 not in nums:
        length = 1
        current = num

        while current + 1 in nums:
            current += 1
            length += 1

        longest = max(longest, length)

print(longest)
