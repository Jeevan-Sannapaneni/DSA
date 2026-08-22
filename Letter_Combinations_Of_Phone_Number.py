

"""
Problem 084: Letter Combinations of a Phone Number

Difficulty: Medium

Problem Statement:
Given a string containing digits from 2 to 9, return all
possible letter combinations that the digits can represent.

The mapping follows a standard phone keypad.

Input:
A string of digits from 2 to 9.

Output:
All possible letter combinations, one per line.

Time Complexity: O(4^N)
Space Complexity: O(N)
"""

digits = input().strip()

phone = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

result = []


def generate(index, current):
    if index == len(digits):
        result.append(current)
        return

    letters = phone[digits[index]]

    for letter in letters:
        generate(index + 1, current + letter)


if digits:
    generate(0, "")

for combination in result:
    print(combination)
