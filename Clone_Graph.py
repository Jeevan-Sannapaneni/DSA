

"""
Problem 074: Clone Graph

Difficulty: Medium

Problem Statement:
Given an undirected graph, create a deep copy of the graph.

The graph contains N nodes numbered from 1 to N.
The input gives the neighbors of every node.

Input:
N
For each node i:
K followed by K neighbor node numbers

Output:
The adjacency list of the cloned graph.

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []


def clone_graph(nodes):
    if not nodes:
        return []

    cloned = {}

    for node in nodes:
        cloned[node.value] = Node(node.value)

    for node in nodes:
        for neighbor in node.neighbors:
            cloned[node.value].neighbors.append(
                cloned[neighbor.value]
            )

    return list(cloned.values())


n = int(input())

nodes = [Node(i) for i in range(1, n + 1)]

for i in range(n):
    data = list(map(int, input().split()))

    count = data[0]
    neighbors = data[1:]

    for neighbor in neighbors[:count]:
        nodes[i].neighbors.append(nodes[neighbor - 1])


cloned_nodes = clone_graph(nodes)

for node in cloned_nodes:
    neighbors = sorted(
        neighbor.value for neighbor in node.neighbors
    )

    print(node.value, *neighbors)
