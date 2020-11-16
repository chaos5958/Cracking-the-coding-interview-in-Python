
def count_num_ways(num_steps):
    mem = [0 for _ in range(num_steps)]
    return _count_num_ways(num_steps, mem)

def _count_num_ways(num_steps, mem):
    if num_steps == 0 or num_steps == 1:
        return 1
    elif num_steps < 0:
        return 0

    num_ways = 0
    if mem[num_steps - 1] != 0:
        return mem[num_steps - 1]
    else:
        num_ways += _count_num_ways(num_steps - 1, mem)
        num_ways += _count_num_ways(num_steps - 2, mem)
        num_ways += _count_num_ways(num_steps - 3, mem)

    return num_ways

import unittest

class Test(unittest.TestCase):
  def test_triple_step(self):
    self.assertEqual(count_num_ways(3), 4)
    self.assertEqual(count_num_ways(7), 44)

if __name__ == "__main__":
  unittest.main()
