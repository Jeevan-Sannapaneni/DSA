"""
Problem 051: Palindrome Linked List

Difficulty: Easy

Problem Statement:
Given a singly linked list, determine whether the sequence
of values reads the same from left to right and right to left.

Input:
N
N space-separated elements

Output:
YES if the linked list is a palindrome, otherwise NO.

Time Complexity: O(N)
Space Complexity: O(1)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def is_palindrome(head):
    if head is None or head.next is None:
        return True

    # Find the middle
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    previous = None
    current = slow

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    # Compare both halves
    first = head
    second = previous

    while second:
        if first.value != second.value:
            return False

        first = first.next
        second = second.next

    return True


n = int(input())
values = list(map(int, input().split()))

head = Node(values[0])
current = head

for value in values[1:]:
    current.next = Node(value)
    current = current.next

print("YES" if is_palindrome(head) else "NO")
