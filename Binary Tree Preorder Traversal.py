"""
Problem 054: Binary Tree Preorder Traversal

Difficulty: Easy

Problem Statement:
Given a binary tree, print its nodes in preorder traversal.

Preorder order:
Root -> Left -> Right

Input:
N
N integers representing the tree in level-order.
Use -1 for a missing node.

Output:
Preorder traversal.

Time Complexity: O(N)
Space Complexity: O(N)
"""

from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree(values):
    if not values or values[0] == -1:
        return None

    root = Node(values[0])
    queue = deque([root])
    index = 1

    while queue and index < len(values):
        current = queue.popleft()

        if index < len(values) and values[index] != -1:
            current.left = Node(values[index])
            queue.append(current.left)
        index += 1

        if index < len(values) and values[index] != -1:
            current.right = Node(values[index])
            queue.append(current.right)
        index += 1

    return root


def preorder(root):
    if root is None:
        return

    print(root.value, end=" ")
    preorder(root.left)
    preorder(root.right)


n = int(input())
values = list(map(int, input().split()))

root = build_tree(values)

preorder(root)
print()
