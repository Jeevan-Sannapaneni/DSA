"""
Problem 048: Remove Nth Node From End

Difficulty: Medium

Problem Statement:
Given a singly linked list, remove the Nth node
from the end of the list and print the resulting list.

Input:
N
List elements
Position from end

Output:
Modified linked list

Time Complexity: O(N)
Space Complexity: O(1)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head

    fast = dummy
    slow = dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next


n = int(input())
values = list(map(int, input().split()))
k = int(input())

head = Node(values[0])
current = head

for value in values[1:]:
    current.next = Node(value)
    current = current.next

head = remove_nth_from_end(head, k)

result = []
current = head

while current:
    result.append(current.value)
    current = current.next

print(*result)
