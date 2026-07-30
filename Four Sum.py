"""
Problem 026: Four Sum

Difficulty: Medium

Problem Statement:
Given an integer array and a target,
print all unique quadruplets whose sum equals the target.

Input:
N
Array
Target

Output:
Unique quadruplets.

Time Complexity: O(N³)
Space Complexity: O(1) (excluding output)
"""

n = int(input())
arr = list(map(int, input().split()))
target = int(input())

arr.sort()

answer = []

for i in range(n - 3):

    if i > 0 and arr[i] == arr[i - 1]:
        continue

    for j in range(i + 1, n - 2):

        if j > i + 1 and arr[j] == arr[j - 1]:
            continue

        left = j + 1
        right = n - 1

        while left < right:

            total = arr[i] + arr[j] + arr[left] + arr[right]

            if total == target:

                answer.append([arr[i], arr[j], arr[left], arr[right]])

                left += 1
                right -= 1

                while left < right and arr[left] == arr[left - 1]:
                    left += 1

                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

            elif total < target:
                left += 1

            else:
                right -= 1

if answer:
    for quad in answer:
        print(*quad)
else:
    print(-1)
