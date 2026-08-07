"""
Problem 040: Min Stack

Difficulty: Medium

Problem Statement:
Design a stack that supports the following operations:

1. PUSH X  - Add X to the stack.
2. POP     - Remove the top element.
3. TOP     - Print the top element.
4. MIN     - Print the minimum element.

MIN must work in O(1) time.

Input:
Q
Q operations

Output:
Print the result for TOP and MIN operations.

Time Complexity:
O(1) per operation

Space Complexity:
O(N)
"""

q = int(input())

stack = []
min_stack = []

for _ in range(q):
    operation = input().split()

    if operation[0] == "PUSH":
        value = int(operation[1])

        stack.append(value)

        if not min_stack:
            min_stack.append(value)
        else:
            min_stack.append(min(value, min_stack[-1]))

    elif operation[0] == "POP":
        if stack:
            stack.pop()
            min_stack.pop()

    elif operation[0] == "TOP":
        if stack:
            print(stack[-1])
        else:
            print("EMPTY")

    elif operation[0] == "MIN":
        if min_stack:
            print(min_stack[-1])
        else:
            print("EMPTY")
