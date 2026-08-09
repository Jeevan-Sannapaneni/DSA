"""
Problem 045: Reverse Linked List

Difficulty: Easy

Problem Statement:
Given a singly linked list, reverse the list and
print the elements of the reversed list.

Input:
N
N space-separated elements

Output:
Reversed linked list

Time Complexity: O(N)
Space Complexity: O(1)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse(head):
    previous = None
    current = head

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


n = int(input())
values = list(map(int, input().split()))

if n == 0:
    print()
else:
    head = Node(values[0])
    current = head

    for value in values[1:]:
        current.next = Node(value)
        current = current.next

    head = reverse(head)

    result = []
    current = head

    while current:
        result.append(current.value)
        current = current.next

    print(*result)
