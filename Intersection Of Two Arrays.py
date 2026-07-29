"""
Problem 023: Intersection Of Two Arrays

Difficulty: Easy

Problem Statement:
Given two integer arrays,
return their unique intersection.

Input:
N M
Array1
Array2

Output:
Common elements in sorted order.

Time Complexity: O(N + M)
Space Complexity: O(N)
"""

n, m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

intersection = sorted(set(arr1) & set(arr2))

if intersection:
    print(*intersection)
else:
    print(-1)
