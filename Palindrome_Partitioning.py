

"""
Problem 085: Palindrome Partitioning

Difficulty: Medium

Problem Statement:
Given a string, partition it so that every substring
in the partition is a palindrome.

Return all possible palindrome partitions.

Input:
A string.

Output:
All valid palindrome partitions, one partition per line.

Time Complexity: O(N * 2^N)
Space Complexity: O(N)
"""


s = input().strip()

result = []


def is_palindrome(left, right):
    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True


def partition(start, current):
    if start == len(s):
        result.append(current[:])
        return

    for end in range(start, len(s)):

        if is_palindrome(start, end):
            current.append(s[start:end + 1])

            partition(end + 1, current)

            current.pop()


partition(0)

for parts in result:
    print(" | ".join(parts))
