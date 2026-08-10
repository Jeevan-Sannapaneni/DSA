"""
Problem 050: Add Two Numbers

Difficulty: Medium

Problem Statement:
Two non-negative integers are represented by linked lists.
Each node contains one digit, and the digits are stored
in reverse order.

Add the two numbers and return the result as a linked list.

Input:
N M
First number digits in reverse order
Second number digits in reverse order

Output:
Sum digits in reverse order

Time Complexity: O(max(N, M))
Space Complexity: O(max(N, M))
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def create_list(values):
    head = Node(values[0])
    current = head

    for value in values[1:]:
        current.next = Node(value)
        current = current.next

    return head


def add_numbers(first, second):
    dummy = Node(0)
    current = dummy
    carry = 0

    while first or second or carry:

        a = first.value if first else 0
        b = second.value if second else 0

        total = a + b + carry

        carry = total // 10
        digit = total % 10

        current.next = Node(digit)
        current = current.next

        if first:
            first = first.next

        if second:
            second = second.next

    return dummy.next


n, m = map(int, input().split())

first_values = list(map(int, input().split()))
second_values = list(map(int, input().split()))

first = create_list(first_values)
second = create_list(second_values)

result_head = add_numbers(first, second)

result = []
current = result_head

while current:
    result.append(current.value)
    current = current.next

print(*result)
