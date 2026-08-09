"""
Problem 047: Linked List Cycle

Difficulty: Easy

Problem Statement:
Given a linked list, determine whether the list contains
a cycle.

The input represents a linked list where the last node
points to the node at the given position.

Position is 0-indexed.
If position = -1, the list has no cycle.

Input:
N
N space-separated values
Position

Output:
YES if a cycle exists, otherwise NO.

Time Complexity: O(N)
Space Complexity: O(1)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


n = int(input())
values = list(map(int, input().split()))
position = int(input())

if n == 0:
    print("NO")
else:
    nodes = [Node(value) for value in values]

    for i in range(n - 1):
        nodes[i].next = nodes[i + 1]

    if position != -1:
        nodes[-1].next = nodes[position]

    if has_cycle(nodes[0]):
        print("YES")
    else:
        print("NO")
