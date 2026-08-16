
"""
Problem 069: Convert Sorted Array to Binary Search Tree

Difficulty: Easy

Problem Statement:
Given a sorted array of distinct integers, construct a
height-balanced Binary Search Tree (BST).

A height-balanced BST has left and right subtrees whose
heights differ by at most 1.

Input:
N
N sorted integers

Output:
The preorder traversal of the constructed BST.

Time Complexity: O(N)
Space Complexity: O(N)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_bst(arr, left, right):
    if left > right:
        return None

    mid = (left + right) // 2

    root = Node(arr[mid])

    root.left = build_bst(arr, left, mid - 1)
    root.right = build_bst(arr, mid + 1, right)

    return root


def preorder(root, result):
    if root is None:
        return

    result.append(root.value)
    preorder(root.left, result)
    preorder(root.right, result)


n = int(input())
arr = list(map(int, input().split()))

root = build_bst(arr, 0, n - 1)

result = []
preorder(root, result)

print(*result)
