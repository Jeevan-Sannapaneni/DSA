"""
Problem 022: Insert Interval

Difficulty: Medium

Problem Statement:
Given a list of non-overlapping sorted intervals,
insert a new interval and merge if necessary.

Input:
N
Intervals
New Interval

Output:
Updated intervals.

Time Complexity: O(N)
Space Complexity: O(N)
"""

n = int(input())

intervals = []

for _ in range(n):
    intervals.append(list(map(int, input().split())))

new_interval = list(map(int, input().split()))

result = []

i = 0

while i < n and intervals[i][1] < new_interval[0]:
    result.append(intervals[i])
    i += 1

while i < n and intervals[i][0] <= new_interval[1]:
    new_interval[0] = min(new_interval[0], intervals[i][0])
    new_interval[1] = max(new_interval[1], intervals[i][1])
    i += 1

result.append(new_interval)

while i < n:
    result.append(intervals[i])
    i += 1

for interval in result:
    print(*interval)
