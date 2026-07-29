"""
Problem 021: Merge Intervals

Difficulty: Medium

Problem Statement:
Given a list of intervals, merge all overlapping intervals.

Input:
N
start1 end1
start2 end2
...

Output:
Merged intervals.

Time Complexity: O(N log N)
Space Complexity: O(N)
"""

n = int(input())

intervals = []

for _ in range(n):
    intervals.append(list(map(int, input().split())))

intervals.sort()

merged = []

for interval in intervals:
    if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
    else:
        merged[-1][1] = max(merged[-1][1], interval[1])

for interval in merged:
    print(*interval)
