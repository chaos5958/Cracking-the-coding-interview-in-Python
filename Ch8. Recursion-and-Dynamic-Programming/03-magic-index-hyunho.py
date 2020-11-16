def find_magic_index(arr):
    return _find_magic_index(arr, 0)

#it could be easier by passing start, end indexes
def _find_magic_index(arr, offset):
    if len(arr) == 1:
        if arr[0] == offset:
            return offset
        else:
            return None

    middle = len(arr) // 2
    if arr[middle] == middle + offset:
        return middle + offset
    elif arr[middle] > middle + offset:
        return _find_magic_index(arr[0:middle], offset)
    else:
        return _find_magic_index(arr[middle+1:], middle + offset + 1)

def find_magic_index_1(arr):
    return _find_magic_index_1(arr, 0, len(arr) - 1)

#it could be easier by passing start, end indexes
def _find_magic_index_1(arr, start, end):
    print(arr, start, end)
    if start > end:
        return None

    if start == end:
        if arr[start] == start:
            return start
        else:
            return None

    middle = (start + end) // 2
    if arr[middle] == middle:
        return middle

    #left
    end_ = min(middle - 1, arr[middle])
    left = _find_magic_index_1(arr, start, end_)
    if left is not None:
        return left

    start_ = max(middle + 1, arr[middle])
    right = _find_magic_index_1(arr, start_, end)

    return right

import unittest

class Test(unittest.TestCase):
  def test_magic_index_1(self):
    #self.assertEqual(find_magic_index_1([3,4,5]), None)
    #self.assertEqual(find_magic_index_1([-2,-1,0,2]), None)
    #self.assertEqual(find_magic_index_1([-20,0,1,2,3,4,5,6,20]), None)
    #self.assertEqual(find_magic_index_1([-20,0,1,2,3,4,5,7,20]), 7)
    #self.assertEqual(find_magic_index_1([-20,1,2,3,4,5,6,20]), 1)
    self.assertEqual(find_magic_index_1([-20,5,5,5,5,5,6,20]), 6)

  def test_magic_index(self):
    self.assertEqual(find_magic_index([3,4,5]), None)
    self.assertEqual(find_magic_index([-2,-1,0,2]), None)
    self.assertEqual(find_magic_index([-20,0,1,2,3,4,5,6,20]), None)
    self.assertEqual(find_magic_index([-20,0,1,2,3,4,5,7,20]), 7)
    #self.assertEqual(find_magic_index([-20,1,2,3,4,5,6,20]), 1)
    #self.assertEqual(find_magic_index([-20,5,5,5,5,5,6,20]), 5)

if __name__ == "__main__":
  unittest.main()

