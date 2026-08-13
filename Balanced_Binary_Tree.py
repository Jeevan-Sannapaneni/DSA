

"""
Problem 061: Balanced Binary Tree

Difficulty: Easy

Problem Statement:
A binary tree is balanced if the height difference
between the left and right subtrees of every node is
at most 1.

Determine whether the given binary tree is balanced.

Input:
N
N space-separated values representing the tree in level-order.
Use -1 for a missing node.

Output:
YES if the tree is balanced, otherwise NO.

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


def height(root):
    if root is None:
        return 0

    left_height = height(root.left)

    if left_height == -1:
        return -1

    right_height = height(root.right)

    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1

    return 1 + max(left_height, right_height)


def is_balanced(root):
    return height(root) != -1


n = int(input())
values = list(map(int, input().split()))

root = build_tree(values)

print("YES" if is_balanced(root) else "NO")
