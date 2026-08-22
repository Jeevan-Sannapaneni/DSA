
"""
Problem 086: N-Queens

Difficulty: Hard

Problem Statement:
Place N queens on an N x N chessboard so that no two
queens attack each other.

Two queens cannot share:
- The same row
- The same column
- The same diagonal

Print all possible valid board configurations.

Input:
N

Output:
Each valid board configuration.
Use Q for a queen and . for an empty cell.

Time Complexity: O(N!)
Space Complexity: O(N)
"""

n = int(input())

board = [
    ["."] * n
    for _ in range(n)
]

result = []

columns = set()
diagonal1 = set()
diagonal2 = set()


def solve(row):

    if row == n:
        result.append(
            ["".join(board[i]) for i in range(n)]
        )
        return

    for col in range(n):

        # Check column.
        if col in columns:
            continue

        # Main diagonal: row - col
        if row - col in diagonal1:
            continue

        # Other diagonal: row + col
        if row + col in diagonal2:
            continue

        # Place queen.
        board[row][col] = "Q"

        columns.add(col)
        diagonal1.add(row - col)
        diagonal2.add(row + col)

        solve(row + 1)

        # Backtrack.
        board[row][col] = "."

        columns.remove(col)
        diagonal1.remove(row - col)
        diagonal2.remove(row + col)


solve(0)

print(len(result))

for solution in result:
    for row in solution:
        print(row)

    print()
