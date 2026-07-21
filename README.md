# Adjacent Difference Parity

## Problem Statement

Given an array of integers, determine whether the absolute difference between every pair of adjacent elements is even. Print **YES** if the condition holds for the entire array; otherwise print **NO**.

### Input

- First line contains an integer `N`.
- Second line contains `N` space-separated integers.

### Output

Print `YES` if every adjacent difference is even, otherwise print `NO`.

### Constraints

- 1 ≤ N ≤ 2 × 10⁵
- 0 ≤ Ai ≤ 10⁹

### Sample Input

```text
5
4 8 10 6 2
```

### Sample Output

```text
YES
```

## Approach

Traverse the array once and compute the absolute difference between adjacent elements. If any difference is odd, print `NO`; otherwise print `YES`.

### Time Complexity

`O(N)`

### Space Complexity

`O(1)`
