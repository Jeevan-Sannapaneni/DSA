
"""
Problem 070: Lowest Common Ancestor in BST

Difficulty: Medium

Problem Statement:
Given a Binary Search Tree and two node values P and Q,
find their lowest common ancestor.

Use the BST property:
- If both values are smaller, move left.
- If both values are greater, move right.
- Otherwise, the current node is the LCA.

Input:
N
N space-separated values of the BST
P Q

Output:
Value of the lowest common ancestor.

Time Complexity: O(H)
Space Complexity: O(1)

H = height of the BST.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


def lowest_common_ancestor(root, p, q):
    current = root

    while current:

        if p < current.value and q < current.value:
            current = current.left

        elif p > current.value and q > current.value:
            current = current.right

        else:
            return current.value

    return -1


n = int(input())
values = list(map(int, input().split()))

p, q = map(int, input().split())

root = None

for value in values:
    root = insert(root, value)

print(lowest_common_ancestor(root, p, q))
