from collections import deque

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def is_subtree(node1, node2):
    if not node2:
        return True
    if not node1:
        return False

    queue = deque()
    queue.append(node1)
    while queue:
        n = queue.popleft()
        if n.data == node2.data:
            if is_sametree(n, node2):
                return True
        if n.left:
            queue.append(n.left)
        if n.right:
            queue.append(n.right)

    return False

def is_sametree(node1, node2):
    if not node1 and not node2:
        return True
    elif not node1 or not node2:
        return False

    if node1.data != node2.data:
        return False

    is_left_same = is_sametree(node1.left, node2.left)
    is_right_same = is_sametree(node1.right, node2.right)

    return is_left_same and is_right_same

import unittest

class Test(unittest.TestCase):
  def test_is_subtree(self):
    tree1 = Node(5,Node(3,Node(2),Node(4)),Node(8,Node(7,Node(9)),Node(1)))
    tree2 = Node(8,Node(7),Node(1))
    self.assertEqual(is_subtree(tree1, tree2), False)
    tree3 = Node(8,Node(7,Node(9)),Node(1))
    self.assertEqual(is_subtree(tree1, tree3), True)

if __name__ == "__main__":
  unittest.main()






