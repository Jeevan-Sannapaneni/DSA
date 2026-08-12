

"""
Problem 057: Maximum Depth of Binary Tree

Difficulty: Easy

Problem Statement:
Given the root of a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest
path from the root node down to the farthest leaf node.

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


def max_depth(root):
    if root is None:
        return 0

    return 1 + max(
        max_depth(root.left),
        max_depth(root.right)
    )


n = int(input())
values = list(map(int, input().split()))

root = build_tree(values)

print(max_depth(root))
