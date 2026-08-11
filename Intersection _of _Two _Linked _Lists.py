"""
Problem 052: Intersection of Two Linked Lists

Difficulty: Easy

Problem Statement:
Given two singly linked lists, determine the value of
the first node where the two lists intersect.

The lists share the same node from the intersection onward.

Input:
N M
First list
Second list
Intersection position in first list
Intersection position in second list

Use -1 if there is no intersection.

Output:
Value of the intersection node, or -1.

Time Complexity: O(N + M)
Space Complexity: O(1)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def get_intersection(head_a, head_b):
    pointer_a = head_a
    pointer_b = head_b

    while pointer_a != pointer_b:

        if pointer_a:
            pointer_a = pointer_a.next
        else:
            pointer_a = head_b

        if pointer_b:
            pointer_b = pointer_b.next
        else:
            pointer_b = head_a

    return pointer_a


n, m = map(int, input().split())

values_a = list(map(int, input().split()))
values_b = list(map(int, input().split()))

pos_a, pos_b = map(int, input().split())

nodes_a = [Node(value) for value in values_a]
nodes_b = [Node(value) for value in values_b]

for i in range(n - 1):
    nodes_a[i].next = nodes_a[i + 1]

for i in range(m - 1):
    nodes_b[i].next = nodes_b[i + 1]

# Connect both lists at the common node
if pos_a != -1 and pos_b != -1:
    nodes_b[pos_b].next = nodes_a[pos_a]

    current = nodes_a[pos_a]

    while current.next:
        current = current.next

    # The shared suffix is already connected through A.

intersection = get_intersection(nodes_a[0], nodes_b[0])

if intersection:
    print(intersection.value)
else:
    print(-1)
