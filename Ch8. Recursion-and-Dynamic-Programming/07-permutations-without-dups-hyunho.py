#permutations -> words
#separate function: insert_char_at
def permutations(string):
    if not string:
        return None

    if len(string) == 1:
        return [string]

    result = []
    words = permutations(string[0:-1])
    for word in words:
        for i in range(len(word) + 1):
            s = insert_char_at(word, string[-1], i)
            result.append(s)

    return result

def insert_char_at(word, c, i):
    return word[0:i] + c + word[i:]

import unittest

class Test(unittest.TestCase):
  def test_permutations(self):
    self.assertEqual(permutations("ABCD"), ["ABCD", "ABDC", "ACBD", "ACDB",
        "ADBC", "ADCB", "BACD", "BADC", "BCAD", "BCDA", "BDAC", "BDCA",
        "CABD", "CADB", "CBAD", "CBDA", "CDAB", "CDBA", "DABC", "DACB",
        "DBAC", "DBCA", "DCAB", "DCBA"])

if __name__ == "__main__":
  unittest.main()

