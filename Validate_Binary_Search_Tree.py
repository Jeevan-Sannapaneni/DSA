
"""
Problem 067: Validate Binary Search Tree

Difficulty: Medium

Problem Statement:
Given a binary tree, determine whether it satisfies
the properties of a Binary Search Tree.

For every node:
- All values in the left subtree must be smaller.
- All values in the right subtree must be greater.

Input:
N
N space-separated values representing the tree in level-order.
Use -1 for a missing node.

Output:
YES if the tree is a valid BST, otherwise NO.

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


def is_valid_bst(root, minimum, maximum):
    if root is None:
        return True

    if not (minimum < root.value < maximum):
        return False

    return (
        is_valid_bst(root.left, minimum, root.value)
        and
        is_valid_bst(root.right, root.value, maximum)
    )


n = int(input())
values = list(map(int, input().split()))

root = build_tree(values)

if is_valid_bst(root, float("-inf"), float("inf")):
    print("YES")
else:
    print("NO")# File: 067_Validate_Binary_Search_Tree.py

"""
Problem 067: Validate Binary Search Tree

Difficulty: Medium

Problem Statement:
Given a binary tree, determine whether it satisfies
the properties of a Binary Search Tree.

For every node:
- All values in the left subtree must be smaller.
- All values in the right subtree must be greater.

Input:
N
N space-separated values representing the tree in level-order.
Use -1 for a missing node.

Output:
YES if the tree is a valid BST, otherwise NO.

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


def is_valid_bst(root, minimum, maximum):
    if root is None:
        return True

    if not (minimum < root.value < maximum):
        return False

    return (
        is_valid_bst(root.left, minimum, root.value)
        and
        is_valid_bst(root.right, root.value, maximum)
    )


n = int(input())
values = list(map(int, input().split()))

root = build_tree(values)

if is_valid_bst(root, float("-inf"), float("inf")):
    print("YES")
else:
    print("NO")
