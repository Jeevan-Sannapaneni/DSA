
"""
Problem 068: Kth Smallest Element in BST

Difficulty: Medium

Problem Statement:
Given a Binary Search Tree and an integer K,
find the Kth smallest element in the BST.

Inorder traversal of a BST produces values
in sorted order.

Input:
N
N space-separated values representing the BST.
K

Output:
The Kth smallest element.

Time Complexity: O(H + K)
Space Complexity: O(H)

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


def kth_smallest(root, k):
    stack = []
    current = root

    while True:

        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        k -= 1

        if k == 0:
            return current.value

        current = current.right


n = int(input())
values = list(map(int, input().split()))
k = int(input())

root = None

for value in values:
    root = insert(root, value)

print(kth_smallest(root, k))
