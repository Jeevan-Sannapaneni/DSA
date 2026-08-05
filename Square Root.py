"""
Problem 038: Square Root Using Binary Search

Difficulty: Easy

Problem Statement:
Given a non-negative integer X,
find the integer square root of X.
(The floor value of the square root.)

Input:
X

Output:
Integer square root

Time Complexity: O(log X)
Space Complexity: O(1)
"""

x = int(input())

if x == 0 or x == 1:
    print(x)
else:

    left = 1
    right = x
    answer = 0

    while left <= right:

        mid = (left + right) // 2

        if mid * mid == x:
            answer = mid
            break

        elif mid * mid < x:
            answer = mid
            left = mid + 1

        else:
            right = mid - 1

    print(answer)
