
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = None

        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self


def successor(tree):
    if tree is None:
        return None

    if tree.right:
        tree = tree.right
        while tree.left:
            tree = tree.left
        return tree
    elif tree.parent:
        parent = tree.parent
        while parent and parent.right == tree:
            tree = parent
            parent = parent.parent
        return parent
    else:
        return None

import unittest

class Test(unittest.TestCase):
  def test_successor(self):
    self.assertEqual(successor(Node(22, Node(11))), None)
    self.assertEqual(successor(Node(22, Node(11), Node(33))).data, 33)
    self.assertEqual(successor(Node(22, Node(11), Node(33, Node(28)))).data, 28)
    self.assertEqual(successor(Node(22, Node(11), Node(33)).left).data, 22)
    self.assertEqual(successor(Node(22, Node(11), Node(33)).right), None)

if __name__ == "__main__":
  unittest.main()
