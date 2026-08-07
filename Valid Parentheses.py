"""
Problem 039: Valid Parentheses

Difficulty: Easy

Problem Statement:
Given a string containing the characters '(', ')', '{', '}',
'[' and ']', determine whether the brackets are balanced.

A valid string must have:
1. Every opening bracket closed by the same type.
2. Brackets closed in the correct order.

Input:
A string

Output:
YES if the string is valid, otherwise NO.

Time Complexity: O(N)
Space Complexity: O(N)
"""

s = input().strip()

stack = []

pairs = {
    ')': '(',
    '}': '{',
    ']': '['
}

valid = True

for ch in s:
    if ch in "([{":
        stack.append(ch)

    else:
        if not stack or stack[-1] != pairs[ch]:
            valid = False
            break

        stack.pop()

if stack:
    valid = False

print("YES" if valid else "NO")
