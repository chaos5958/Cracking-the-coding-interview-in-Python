class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def is_bst(tree):
    if not tree:
        return False, None, None

    if tree.left and tree.right:
        is_right_bst, right_min, right_max = is_bst(tree.right)
        is_left_bst, left_min, left_max = is_bst(tree.left)
        return right_min > tree.data >= left_max and is_left_bst and is_right_bst, \
            min(left_min, right_min, tree.data), max(left_max, right_max, tree.data)
    elif tree.left:
        is_left_bst, left_min, left_max = is_bst(tree.left)
        return tree.data >= left_max and is_left_bst, min(left_min, tree.data), max(left_max, tree.data)
    elif tree.right:
        is_right_bst, right_min, right_max = is_bst(tree.right)
        return tree.data < right_min and is_right_bst, min(right_min, tree.data), max(right_max, tree.data)
    else:
        return True, tree.data, tree.data

import unittest

class Test(unittest.TestCase):
    def test_validate_tree(self):
        self.assertEqual(is_bst(Node(3,Node(1),Node(8)))[0], True)
        tree1 = Node(5,Node(3,Node(1),Node(4)),Node(7,Node(6),Node(8,None,Node(9))))
        self.assertEqual(is_bst(tree1)[0], True)
        tree2 = Node(7,Node(3,Node(1),Node(8)),Node(9,Node(8),Node(11)))
        self.assertEqual(is_bst(tree2)[0], False)

if __name__ == "__main__":
    unittest.main()
