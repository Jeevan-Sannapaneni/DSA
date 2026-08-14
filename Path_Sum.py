

"""
Problem 064: Path Sum

Difficulty: Easy

Problem Statement:
Given a binary tree and a target sum, determine whether
there exists a root-to-leaf path whose node values add up
to the target sum.

Input:
N
N space-separated values representing the tree in level-order.
Use -1 for a missing node.
Target sum

Output:
YES if such a path exists, otherwise NO.

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


def has_path_sum(root, target):
    if root is None:
        return False

    target -= root.value

    if root.left is None and root.right is None:
        return target == 0

    return (
        has_path_sum(root.left, target)
        or has_path_sum(root.right, target)
    )


n = int(input())
values = list(map(int, input().split()))
target = int(input())

root = build_tree(values)

print("YES" if has_path_sum(root, target) else "NO")
