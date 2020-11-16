def multiply(a, b):
    if a == 1 or b == 1:
        return max(a, b)

    min_value = min(a, b)
    max_value = max(a, b)

    num_shift = 0
    num_add = 0
    num_sub = 0

    value = 1
    while value < min_value:
        value = value << 1
        num_shift += 1

    if value - min_value > min_value - (value >> 1):
        num_shift -= 1
        num_add = min_value - (value >> 1)
    elif value - min_value < min_value - (value >> 1):
        num_sub = value - min_value

    result = max_value
    print(num_shift, num_add, num_sub)
    for _ in range(num_shift):
        result = result << 1
    for _ in range(num_add):
        result += max_value
    for _ in range(num_sub):
        result -= max_value

    return result

def multiply1(a, b):
    smaller = min(a, b)
    bigger = max(a, b)
    return _multiply1(smaller, bigger)

def _multiply1(smaller, bigger):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger

    s = smaller >> 1
    half = _multiply1(s, bigger)

    if smaller % 2 == 0:
        return half + half
    else:
        return half + half + bigger

import unittest

class Test(unittest.TestCase):
  def test_multiply(self):
    self.assertEqual(multiply1(2, 2), 4)
    self.assertEqual(multiply1(1, 125), 125)
    self.assertEqual(multiply1(7, 11), 77)
    self.assertEqual(multiply1(10000000010, 21), 210000000210)

if __name__ == "__main__":
  unittest.main()

