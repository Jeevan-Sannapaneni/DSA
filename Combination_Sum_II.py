"""
Problem 083: Combination Sum II

Difficulty: Medium

Problem Statement:
Given an array of positive integers and a target value,
find all unique combinations whose sum equals the target.

Each element can be used at most once.

The input may contain duplicate values, but duplicate
combinations must not appear.

Input:
N
N space-separated integers
Target

Output:
All unique combinations whose sum equals the target.

Time Complexity: O(2^N)
Space Complexity: O(N)
"""


n = int(input())
arr = list(map(int, input().split()))
target = int(input())

arr.sort()

result = []


def find_combinations(start, remaining, current):

    if remaining == 0:
        result.append(current[:])
        return

    for i in range(start, n):

        # Skip duplicate values at the same level.
        if i > start and arr[i] == arr[i - 1]:
            continue

        if arr[i] > remaining:
            break

        current.append(arr[i])

        # Move to the next element because each element
        # can be used only once.
        find_combinations(
            i + 1,
            remaining - arr[i],
            current
        )

        current.pop()


find_combinations(0, target, [])

for combination in result:
    print(*combination)
