"""
Problem 049: Middle of Linked List

Difficulty: Easy

Problem Statement:
Given a singly linked list, find the middle element.

If the list has two middle elements, return the second one.

Input:
N
List elements

Output:
Middle element

Time Complexity: O(N)
Space Complexity: O(1)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.value


n = int(input())
values = list(map(int, input().split()))

head = Node(values[0])
current = head

for value in values[1:]:
    current.next = Node(value)
    current = current.next

print(find_middle(head))
