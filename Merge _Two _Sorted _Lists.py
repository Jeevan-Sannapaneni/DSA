"""
Problem 046: Merge Two Sorted Lists

Difficulty: Easy

Problem Statement:
Given two sorted linked lists, merge them into a single
sorted linked list.

Input:
N M
First sorted list
Second sorted list

Output:
Merged sorted list

Time Complexity: O(N + M)
Space Complexity: O(1) excluding output
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def create_list(values):
    if not values:
        return None

    head = Node(values[0])
    current = head

    for value in values[1:]:
        current.next = Node(value)
        current = current.next

    return head


def merge_lists(first, second):
    dummy = Node(0)
    current = dummy

    while first and second:

        if first.value <= second.value:
            current.next = first
            first = first.next
        else:
            current.next = second
            second = second.next

        current = current.next

    if first:
        current.next = first
    else:
        current.next = second

    return dummy.next


n, m = map(int, input().split())

first_values = list(map(int, input().split()))
second_values = list(map(int, input().split()))

first = create_list(first_values)
second = create_list(second_values)

head = merge_lists(first, second)

result = []
current = head

while current:
    result.append(current.value)
    current = current.next

print(*result)
