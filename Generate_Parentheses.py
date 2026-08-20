

"""
Problem 078: Generate Parentheses

Difficulty: Medium

Problem Statement:
Given N pairs of parentheses, generate all combinations
of well-formed parentheses.

Input:
N

Output:
All valid combinations.

Time Complexity: O(4^N / sqrt(N))
Space Complexity: O(N)
"""


n = int(input())

result = []


def generate(current, opening, closing):
    # A complete valid combination is formed.
    if len(current) == 2 * n:
        result.append(current)
        return

    # Add an opening bracket if available.
    if opening < n:
        generate(
            current + "(",
            opening + 1,
            closing
        )

    # Add a closing bracket only when it is valid.
    if closing < opening:
        generate(
            current + ")",
            opening,
            closing + 1
        )


generate("", 0, 0)

for combination in result:
    print(combination)
