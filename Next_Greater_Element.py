"""
Problem 041: Next Greater Element

Difficulty: Medium

Problem Statement:
For every element in an array, find the first element
to its right that is greater than it.

If no greater element exists, output -1.

Input:
N
Array

Output:
Next greater element for every position.

Time Complexity: O(N)
Space Complexity: O(N)
"""

n = int(input())
arr = list(map(int, input().split()))

answer = [-1] * n
stack = []

for i in range(n - 1, -1, -1):

    while stack and stack[-1] <= arr[i]:
        stack.pop()

    if stack:
        answer[i] = stack[-1]

    stack.append(arr[i])

print(*answer)
