
"""
Problem 065: Binary Search Tree Search

Difficulty: Easy

Problem Statement:
Given the root of a Binary Search Tree (BST) and a target
value, determine whether the target exists in the tree.

In a BST:
- Values smaller than a node are in its left subtree.
- Values greater than a node are in its right subtree.

Input:
N
N space-separated values representing the BST in level-order.
Use -1 for a missing node.
Target

Output:
YES if the target exists, otherwise NO.

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


def search(root, target):
    current = root

    while current:
        if current.value == target:
            return True

        if target < current.value:
            current = current.left
        else:
            current = current.right

    return False


n = int(input())
values = list(map(int, input().split()))
target = int(input())

root = None

for value in values:
    if value != -1:
        root = insert(root, value)

print("YES" if search(root, target) else "NO")
