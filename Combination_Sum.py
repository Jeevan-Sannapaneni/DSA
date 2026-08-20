
"""
Problem 080: Combination Sum

Difficulty: Medium

Problem Statement:
Given an array of positive integers and a target value,
find all unique combinations of numbers whose sum equals
the target.

Each number may be used multiple times.

Input:
N
N space-separated positive integers
Target

Output:
All combinations whose sum equals the target.

Time Complexity: O(N^T)
Space Complexity: O(T)

T = target value.
"""


n = int(input())
candidates = list(map(int, input().split()))
target = int(input())

candidates.sort()

result = []


def find_combinations(start, remaining, current):
    if remaining == 0:
        result.append(current[:])
        return

    for i in range(start, n):

        if candidates[i] > remaining:
            break

        current.append(candidates[i])

        # Use the same element again.
        find_combinations(
            i,
            remaining - candidates[i],
            current
        )

        current.pop()


find_combinations(0, target, [])

for combination in result:
    print(*combination)
