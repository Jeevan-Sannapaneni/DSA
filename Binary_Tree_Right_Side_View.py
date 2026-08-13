

"""
Problem 060: Binary Tree Right Side View

Difficulty: Medium

Problem Statement:
Given a binary tree, imagine standing on its right side.
Return the values of the nodes that are visible from
the right side, from top to bottom.

Input:
N
N space-separated values representing the tree in level-order.
Use -1 for a missing node.

Output:
Nodes visible from the right side.

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


def right_side_view(root):
    if root is None:
        return []

    queue = deque([root])
    result = []

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            current = queue.popleft()

            if i == level_size - 1:
                result.append(current.value)

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

    return result


n = int(input())
values = list(map(int, input().split()))

root = build_tree(values)

print(*right_side_view(root))
