
"""
Problem 063: Lowest Common Ancestor

Difficulty: Medium

Problem Statement:
Given a binary tree and two node values p and q,
find their lowest common ancestor (LCA).

The lowest common ancestor is the deepest node that
has both p and q in its subtree.

Input:
N
N space-separated values representing the tree in level-order.
Use -1 for a missing node.
p q

Output:
Value of the lowest common ancestor.

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


def lowest_common_ancestor(root, p, q):
    if root is None:
        return None

    if root.value == p or root.value == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right


n = int(input())
values = list(map(int, input().split()))

p, q = map(int, input().split())

root = build_tree(values)

ancestor = lowest_common_ancestor(root, p, q)

if ancestor:
    print(ancestor.value)
else:
    print(-1)
