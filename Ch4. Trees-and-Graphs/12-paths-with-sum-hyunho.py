class Node:
    def __init__(self, name, data, left=None, right=None):
        self.name = name
        self.data = data
        self.left = left
        self.right = right

from collections import Counter

def count_path_with_sum(node, target_sum):
    return _count_path_with_sum(node, target_sum, 0, Counter())

def _count_path_with_sum(node, target_sum, running_sum, path_count):
    if node is None:
        return 0

    running_sum += node.data
    total_paths = path_count[running_sum - target_sum]

    if running_sum == target_sum:
        total_paths += 1

    path_count[running_sum] += 1
    total_paths += _count_path_with_sum(node.left, target_sum, running_sum, path_count)
    total_paths += _count_path_with_sum(node.right, target_sum, running_sum, path_count)
    path_count[running_sum] -= 1

    return total_paths

import unittest

class Test(unittest.TestCase):
  def test_paths_with_sum(self):
    bt=Node("A",4,Node("B",-2,Node("D",7),Node("E", 4)),
                  Node("C", 7,Node("F",-1,Node("H",-1),Node("I",2,Node("K",1))),
                              Node("G", 0,None,        Node("J", -2))))
    print(count_path_with_sum(bt, 2))
    print(count_path_with_sum(bt, 12))
    print(count_path_with_sum(bt, 9))
    #self.assertEqual(paths_with_sum(bt, 2), [["A", "B"], ["B", "E"], ["I"],
    #    ["F", "I", "K"]])
    #self.assertEqual(paths_with_sum(bt, 12), [["A", "C", "F", "I"]])
    #self.assertEqual(paths_with_sum(bt, 9), [["A","B","D"], ["A","C","F","H"],
    #    ["C","F","I","K"], ["A","C","G","J"]])

if __name__ == "__main__":
  unittest.main()
