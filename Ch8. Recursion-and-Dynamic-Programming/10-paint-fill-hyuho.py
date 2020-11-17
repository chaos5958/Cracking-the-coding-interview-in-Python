def paint_fill(screen, row, column, new_color):
    if screen[row][column] == new_color:
        return

    old_color = screen[row][column]
    _paint_fill(screen, row, column, new_color, old_color)

def _paint_fill(screen, row, column, new_color, old_color):
    if row < 0 or row >= len(screen):
        return
    if column < 0 or column >= len(screen[0]):
        return
    if screen[row][column] != old_color:
        return

    screen[row][column] = new_color
    _paint_fill(screen, row - 1, column, new_color, old_color)
    _paint_fill(screen, row + 1, column, new_color, old_color)
    _paint_fill(screen, row, column - 1, new_color, old_color)
    _paint_fill(screen, row, column + 1, new_color, old_color)

import unittest

class Test(unittest.TestCase):
  def test_paint_fill(self):
    image1 = [[10, 10, 10, 10, 10, 10, 10, 40],
              [30, 20, 20, 10, 10, 40, 40, 40],
              [10, 10, 20, 20, 10, 10, 10, 10],
              [10, 10, 30, 20, 20, 20, 20, 10],
              [40, 40, 10, 10, 10, 10, 10, 10]]
    image2 = [[30, 30, 30, 30, 30, 30, 30, 40],
              [30, 20, 20, 30, 30, 40, 40, 40],
              [10, 10, 20, 20, 30, 30, 30, 30],
              [10, 10, 30, 20, 20, 20, 20, 30],
              [40, 40, 30, 30, 30, 30, 30, 30]]
    image3 = [[30, 30, 30, 30, 30, 30, 30, 40],
              [30, 20, 20, 30, 30, 40, 40, 40],
              [30, 30, 20, 20, 30, 30, 30, 30],
              [30, 30, 30, 20, 20, 20, 20, 30],
              [40, 40, 30, 30, 30, 30, 30, 30]]
    paint_fill(image1, 1, 3, 30)
    self.assertEqual(image1, image2)
    paint_fill(image1, 1, 3, 10)
    paint_fill(image1, 1, 3, 30)
    self.assertEqual(image1, image3)

if __name__ == "__main__":
  unittest.main()

