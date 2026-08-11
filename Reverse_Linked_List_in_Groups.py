"""
Problem 053: Reverse Linked List in Groups

Difficulty: Hard

Problem Statement:
Given a singly linked list and an integer K,
reverse the nodes of the list in groups of K.

If the remaining nodes contain fewer than K elements,
leave them unchanged.

Input:
N K
N space-separated elements

Output:
Modified linked list

Time Complexity: O(N)
Space Complexity: O(1)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_in_groups(head, k):
    dummy = Node(0)
    dummy.next = head

    group_previous = dummy

    while True:

        # Find the kth node
        kth = group_previous

        for _ in range(k):
            kth = kth.next

            if kth is None:
                return dummy.next

        group_next = kth.next

        # Reverse current group
        previous = group_next
        current = group_previous.next

        while current != group_next:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        # Connect previous group
        old_start = group_previous.next
        group_previous.next = kth
        group_previous = old_start


n, k = map(int, input().split())
values = list(map(int, input().split()))

head = Node(values[0])
current = head

for value in values[1:]:
    current.next = Node(value)
    current = current.next

head = reverse_in_groups(head, k)

result = []
current = head

while current:
    result.append(current.value)
    current = current.next

print(*result)
