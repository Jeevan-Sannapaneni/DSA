"""
Problem 056: Binary Tree Level Order Traversal

Difficulty: Medium

Problem Statement:
Given a binary tree, print its nodes level by level
from left to right.

Input:
N
N integers representing the tree in level-order.
Use -1 for a missing node.

Output:
Level-order traversal.

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


def level_order(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        current = queue.popleft()

        print(current.value, end=" ")

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)


n = int(input())
values = list(map(int, input().split()))

root = build_tree(values)

level_order(root)
print()
