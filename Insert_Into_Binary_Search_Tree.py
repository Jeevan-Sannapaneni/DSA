

"""
Problem 066: Insert Into Binary Search Tree

Difficulty: Medium

Problem Statement:
Given a Binary Search Tree (BST) and a value,
insert the value into the BST while maintaining
the BST property.

Input:
N
N space-separated values representing the BST
Value to insert

Output:
The BST after insertion in inorder traversal.

Time Complexity: O(H)
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


def inorder(root, result):
    if root is None:
        return

    inorder(root.left, result)
    result.append(root.value)
    inorder(root.right, result)


n = int(input())
values = list(map(int, input().split()))
value = int(input())

root = None

for number in values:
    root = insert(root, number)

root = insert(root, value)

result = []
inorder(root, result)

print(*result)
