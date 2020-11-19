from collections import Counter

def count_all_ways(string, boolean):
    if not string:
        return 0

    mem = {}
    if boolean:
        return _count_all_ways(string, mem)[0]
    else:
        return _count_all_ways(string, mem)[1]


def _count_all_ways(string, mem):
    if len(string) == 1:
        if string == '1':
            return (1, 0)
        else:
            return (0, 1)

    if string in mem:
        return mem[string]

    true_counts = 0
    false_counts = 0

    i = 1
    while i <= len(string) - 1:
        (left_true_counts, left_false_counts) = _count_all_ways(string[0:i], mem)
        (right_true_counts, right_false_counts) = _count_all_ways(string[i+1:], mem)

        sub_total_counts = (left_true_counts + left_false_counts) * (right_true_counts + right_false_counts)
        if string[i] == '&':
            sub_true_counts = left_true_counts * right_true_counts
            sub_false_counts = sub_total_counts - sub_true_counts
        elif string[i] == '|':
            sub_false_counts = left_false_counts * right_false_counts
            sub_true_counts = sub_total_counts - sub_false_counts
            pass
        elif string[i] == '^':
            sub_true_counts = left_false_counts * right_true_counts + left_true_counts * right_false_counts
            sub_false_counts = sub_total_counts - sub_true_counts
        true_counts += sub_true_counts
        false_counts += sub_false_counts
        i += 2

    mem[string] = (true_counts, false_counts)

    return (true_counts, false_counts)

import unittest

class Test(unittest.TestCase):
  def test_count_eval(self):
    self.assertEqual(count_all_ways("1", True), 1)
    self.assertEqual(count_all_ways("0", True), 0)
    self.assertEqual(count_all_ways("0", False), 1)
    self.assertEqual(count_all_ways("1&1", True), 1)
    self.assertEqual(count_all_ways("1|0", False), 0)
    self.assertEqual(count_all_ways("1^0", True), 1)
    self.assertEqual(count_all_ways("1&0&1", True), 0)
    self.assertEqual(count_all_ways("1|1^0", True), 2)
    self.assertEqual(count_all_ways("1^0|0|1", False), 2)
    self.assertEqual(count_all_ways("1^0|0|1", True), 3)
    self.assertEqual(count_all_ways("0&0&0&1^1|0", True), 10)

if __name__ == "__main__":
  unittest.main()

