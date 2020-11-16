import copy

def find_path_old(grid):
    if not grid or len(grid) == 0 or len(grid[0]) == 0:
        return None
    column = len(grid[0])
    row  = len(grid)
    path = []
    solution = []
    path.append("end")
    _find_path(grid, column - 1, row - 1, path, solution)

    if len(solution) > 0:
        return solution[0]
    else:
        return None

def _find_path_old(grid, column, row, path, solution):
    if column == 0 and row == 0:
        path.insert(0, "start")
        solution.append(copy.deepcopy(path))
    if grid[row][column] == 1:
        return

    if column == 0:
        path.insert(0, "down")
        _find_path(grid, column, row - 1, path, solution)
        path.pop(0)
    elif row == 0:
        path.insert(0, "right")
        _find_path(grid, column - 1, row, path, solution)
        path.pop(0)
    else:
        path.insert(0, "right")
        _find_path(grid, column - 1, row, path, solution)
        path.pop(0)
        path.insert(0, "down")
        _find_path(grid, column, row - 1, path, solution)
        path.pop(0)

from collections import Counter

def find_path(grid):
    if not grid or len(grid) == 0 or len(grid[0]) == 0:
        return None
    column = len(grid[0])
    row  = len(grid)
    path = []
    solution = []
    mem = Counter()

    if _find_path(grid, column - 1, row - 1, path, mem):
        path.append("end")
        return path

    return None

def _find_path(grid, column, row, path, mem):
    if column < 0 or row < 0 or grid[row][column]:
        return False

    if mem[(column, row)]:
        return False

    is_origin = column == 0 and row == 0
    if is_origin:
        path.append("start")
        return True
    elif _find_path(grid, column -  1, row, path, mem):
        path.append("right")
        return True
    elif _find_path(grid, column, row - 1, path, mem):
        path.append("down")
        return True

    mem[(column, row)] = 1
    return False

import unittest

class Test(unittest.TestCase):
  def test_path_through_grid(self):
    grid = [[0, 0, 0, 0, 0, 0, 1],
            [0, 1, 1, 0, 1, 1, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 1, 0]]
    self.assertEqual(find_path(grid), ["start", "right", "right",
            "right", "down", "down", "right", "right", "right", "down", "end"])
    grid = [[0, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [1, 1, 0, 0, 0, 1, 0]]
    self.assertEqual(find_path(grid), None)

if __name__ == "__main__":
  unittest.main()

