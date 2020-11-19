class Box:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

from collections import Counter

def max_height(boxes):
    mem = Counter()
    return _max_height(boxes, mem, float('inf'), float('inf'), float('inf'))

def is_valid_box(box, width, height, depth):
    if box.width < width and box.height < height and box.depth < depth:
        return True
    else:
        return False

#we can just pass the index of the bottom box

def _max_height(boxes, mem, width, height, depth):
    max_height = 0

    for i in range(len(boxes)):
        if is_valid_box(boxes[i], width, height, depth):
            box = boxes.pop(i)
            next_width = box.width
            next_height = box.height
            next_depth = box.depth

            if mem[(next_width, next_height, next_depth)]:
                child_height = mem[(next_width, next_height, next_depth)]
            else:
                child_height = _max_height(boxes, mem, next_width, next_height, next_depth)

            if box.height + child_height > max_height:
                max_height = box.height + child_height

            boxes.insert(i, box)
            mem[(width, height, depth)] = max_height

    return max_height

import unittest

class Test(unittest.TestCase):
  def test_stack_boxes(self):
    boxes = [Box(100, 100, 100)]
    self.assertEqual(max_height(boxes), 100)
    boxes.append(Box(25, 25, 25))
    self.assertEqual(max_height(boxes), 125)
    boxes.append(Box(5, 20, 30))
    boxes.append(Box(4, 17, 28))
    self.assertEqual(max_height(boxes), 137)

if __name__ == "__main__":
  unittest.main()

