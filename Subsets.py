

"""
Problem 079: Subsets

Difficulty: Medium

Problem Statement:
Given an array of distinct integers, generate all possible
subsets of the array.

The empty subset must also be included.

Input:
N
N space-separated integers

Output:
All possible subsets, one subset per line.

Time Complexity: O(N * 2^N)
Space Complexity: O(N)
"""


n = int(input())
arr = list(map(int, input().split()))

result = []


def generate(index, current):
    if index == n:
        result.append(current[:])
        return

    # Do not include the current element.
    generate(index + 1, current)

    # Include the current element.
    current.append(arr[index])

    generate(index + 1, current)

    current.pop()


generate(0, [])

for subset in result:
    if subset:
        print(*subset)
    else:
        print("EMPTY")
