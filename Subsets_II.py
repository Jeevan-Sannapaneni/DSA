

"""
Problem 082: Subsets II

Difficulty: Medium

Problem Statement:
Given an array that may contain duplicate integers,
generate all unique subsets.

Duplicate subsets must not appear in the output.

Input:
N
N space-separated integers

Output:
All unique subsets, one per line.

Time Complexity: O(N * 2^N)
Space Complexity: O(N)
"""


n = int(input())
arr = list(map(int, input().split()))

arr.sort()

result = []


def generate(index, current):
    result.append(current[:])

    for i in range(index, n):

        # Skip duplicate values at the same level.
        if i > index and arr[i] == arr[i - 1]:
            continue

        current.append(arr[i])

        generate(i + 1, current)

        current.pop()


generate(0)

for subset in result:
    if subset:
        print(*subset)
    else:
        print("EMPTY")
