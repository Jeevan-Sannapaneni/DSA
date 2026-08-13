

"""
Problem 062: Diameter of Binary Tree

Difficulty: Easy

Problem Statement:
The diameter of a binary tree is the length of the
longest path between any two nodes.

The answer is measured in number of edges.

Input:
N
N space-separated values representing the tree in level-order.
Use -1 for a missing node.

Output:
Diameter of the binary tree.

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


diameter = 0


def height(root):
    global diameter

    if root is None:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    diameter = max(
        diameter,
        left_height + right_height
    )

    return 1 + max(left_height, right_height)


n = int(input())
values = list(map(int, input().split()))

root = build_tree(values)

height(root)

print(diameter)
