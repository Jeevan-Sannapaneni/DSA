"""
Problem 025: Three Sum

Difficulty: Medium

Problem Statement:
Given an integer array, print all unique triplets
whose sum is equal to zero.

Input:
N
Array

Output:
Unique triplets.

Time Complexity: O(N²)
Space Complexity: O(1) (excluding output)
"""

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

result = []

for i in range(n - 2):

    if i > 0 and arr[i] == arr[i - 1]:
        continue

    left = i + 1
    right = n - 1

    while left < right:

        total = arr[i] + arr[left] + arr[right]

        if total == 0:
            result.append([arr[i], arr[left], arr[right]])

            left += 1
            right -= 1

            while left < right and arr[left] == arr[left - 1]:
                left += 1

            while left < right and arr[right] == arr[right + 1]:
                right -= 1

        elif total < 0:
            left += 1

        else:
            right -= 1

if result:
    for triplet in result:
        print(*triplet)
else:
    print(-1)
