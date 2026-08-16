"""
Problem 071: Binary Tree Maximum Path Sum

Difficulty: Hard

Problem Statement:
Given a binary tree, find the maximum possible sum
of values along any path.

A path may start and end at any two nodes, but it must
follow connected parent-child relationships.

Input:
N
N space-separated values representing the tree
in level-order.

Use -1 for a missing node.

Output:
Maximum path sum.

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


maximum_sum = float("-inf")


def max_gain(root):
    global maximum_sum

    if root is None:
        return 0

    left_gain = max(0, max_gain(root.left))
    right_gain = max(0, max_gain(root.right))

    current_path = (
        root.value
        + left_gain
        + right_gain
    )

    maximum_sum = max(maximum_sum, current_path)

    return root.value + max(left_gain, right_gain)


n = int(input())
values = list(map(int, input().split()))

root = build_tree(values)

max_gain(root)

print(maximum_sum)
