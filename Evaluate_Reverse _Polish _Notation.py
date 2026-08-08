"""
Problem 043: Evaluate Reverse Polish Notation

Difficulty: Medium

Problem Statement:
Evaluate an arithmetic expression written in
Reverse Polish Notation (postfix notation).

The expression contains integers and operators:
+, -, *, /

Division truncates toward zero.

Input:
N
N tokens

Output:
Result of the expression.

Time Complexity: O(N)
Space Complexity: O(N)
"""

n = int(input())
tokens = input().split()

stack = []

for token in tokens:

    if token not in {"+", "-", "*", "/"}:
        stack.append(int(token))

    else:
        b = stack.pop()
        a = stack.pop()

        if token == "+":
            result = a + b

        elif token == "-":
            result = a - b

        elif token == "*":
            result = a * b

        else:
            # Truncate division toward zero
            result = int(a / b)

        stack.append(result)

print(stack[-1])
