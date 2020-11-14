def first_common_ancestor(node1, node2):
    node1_parents = []
    while node1.parent:
        node1_parents.append(node1.parent)
        node1 = node1.parent

    target_node = None
    while node2.parent:
        if node2.parent in node1_parents:
            target_node = node2.parent
            break
        node2 = node2.parent
    return target_node

#solution
def first_common_acestor(node1, node2):
    delta = depth(p) - depth(q)
    first = q if delta > 0 else p
    second = p if delta > 0 else q
    second = goUpBy(second)

    while (first != second and first and second):
        first = first.parent
        second = second.parent

    if not first or not second:
        return None
    else:
        return first

def goUpBy(node, delta):
    while (delta > 0 and node):
        node = node.parent
        delta -= 1
    return node

def depth(node):
    depth = 0
    while node.parent:
        depth += 1
        node = node.parent
    return depth

class Node():
  def __init__(self, data=None, left=None, right=None):
    self.data, self.left, self.right = data, left, right
    self.parent = None
    if self.left:
      self.left.parent = self
    if self.right:
      self.right.parent = self

import unittest

class Test(unittest.TestCase):
  def test_first_common_ancestor(self):
    node1 = Node(11, Node(55), Node(77, Node(44)))
    node2 = Node(22, Node(99))
    self.assertEqual(first_common_ancestor(node1, node2), None)
    node3 = Node(33, node1, Node(88, Node(123, None, node2)))
    node4 = Node(44, node3, Node(66))
    self.assertEqual(first_common_ancestor(node1, node2), node3)

if __name__ == "__main__":
  unittest.main()
