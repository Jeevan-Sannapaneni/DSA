

"""
Problem 081: Permutations

Difficulty: Medium

Problem Statement:
Given an array of distinct integers, generate all possible
permutations of the array.

Input:
N
N space-separated integers

Output:
All possible permutations, one per line.

Time Complexity: O(N * N!)
Space Complexity: O(N)
"""


n = int(input())
arr = list(map(int, input().split()))

result = []


def generate(index):
    if index == n:
        result.append(arr[:])
        return

    for i in range(index, n):
        # Choose
        arr[index], arr[i] = arr[i], arr[index]

        # Explore
        generate(index + 1)

        # Backtrack
        arr[index], arr[i] = arr[i], arr[index]


generate(0)

for permutation in result:
    print(*permutation)
