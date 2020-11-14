def all_sequences(node):
    result = []
    if not node:
        result.append([])
        return result

    prefix = []
    prefix.append(node.data)

    left_sequences = all_sequences(node.left)
    right_sequences = all_sequences(node.right)

    print(left_sequences, right_sequences)

    for left in left_sequences:
        for right in right_sequences:
            weaved = []
            weave_lists(left, right, weaved, prefix)
            result += weaved

    return result

import copy

def weave_lists(left, right, weaved, prefix):
    if len(left) == 0 or len(right) == 0:
        result = copy.deepcopy(prefix)
        result += right + left
        weaved.append(result)
        return

    prefix.append(left[0])
    weave_lists(left[1:], right, weaved, prefix)

    prefix.pop()
    prefix.append(right[0])
    weave_lists(left, right[1:], weaved, prefix)
    prefix.pop()

class Node():
  def __init__(self, data=None, left=None, right=None):
    self.data, self.left, self.right = data, left, right

import unittest

class Test(unittest.TestCase):
  def test_bst_sequences(self):
    self.assertEqual(all_sequences(Node(7,Node(4,None, Node(5)),Node(9))), [
      [7, 4, 5, 9],
      [7, 4, 9, 5],
      [7, 9, 4, 5]])
    self.assertEqual(all_sequences(Node(7,Node(4,Node(5),Node(6)),Node(9))), [
      [7, 4, 9, 5, 6],
      [7, 4, 9, 6, 5],
      [7, 4, 5, 9, 6],
      [7, 4, 5, 6, 9],
      [7, 4, 6, 9, 5],
      [7, 4, 6, 5, 9],
      [7, 9, 4, 5, 6],
      [7, 9, 4, 6, 5]])


if __name__ == "__main__":
  unittest.main()

