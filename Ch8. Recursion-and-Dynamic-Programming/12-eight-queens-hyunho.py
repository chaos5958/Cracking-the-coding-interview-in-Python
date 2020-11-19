from collections import Counter

def print_eight_queens(n):
    queens = []
    rows = [i for i in range(n)]
    column = 0
    mem1 = Counter()
    mem2 = Counter()
    _print_eight_queens(n, queens, rows, 0, mem1, mem2)

def _print_eight_queens(n, queens, rows, column, mem1, mem2):
    if len(queens) == n:
        print(queens)

    for i in range(len(rows)):
        curr_row = rows.pop(i)
        if mem1[curr_row + column] or mem2[curr_row - column]:
            rows.insert(i, curr_row)
            continue
        else:
            mem1[curr_row + column] = 1
            mem2[curr_row - column] = 1
            queens.append((curr_row, column))
            _print_eight_queens(n, queens, rows, column + 1, mem1, mem2)
            rows.insert(i, curr_row)
            mem1[curr_row + column] = 0
            mem2[curr_row - column] = 0
            queens.pop()

print_eight_queens(4)
