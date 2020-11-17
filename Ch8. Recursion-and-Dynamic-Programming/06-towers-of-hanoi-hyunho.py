def move_disks(tower1, tower2, tower3):
    total_disks = len(tower1.disks)
    _move_disks(total_disks, tower1, tower3, tower2)

def _move_disks(total_disks, origin, destination, buffer):
    if total_disks <= 0:
        return

    _move_disks(total_disks - 1, origin, buffer, destination)
    destination.disks.append(origin.disks.pop())
    _move_disks(total_disks - 1, buffer, destination, origin)

import unittest

class Tower():
    def __init__(self, name, disks=None):
        self.name = name
        if disks:
            self.disks = disks
        else:
            self.disks = []

class Test(unittest.TestCase):
  def test_towers_of_hanoi(self):
    tower1 = Tower("Tower1", ["6", "5", "4", "3", "2", "1"])
    tower2 = Tower("Tower2")
    tower3 = Tower("Tower3")
    move_disks(tower1, tower2, tower3)
    print(tower1.disks)
    print(tower2.disks)
    print(tower3.disks)
    self.assertEqual(tower1.disks, [])
    self.assertEqual(tower2.disks, [])
    self.assertEqual(tower3.disks, ["6", "5", "4", "3", "2", "1"])

if __name__ == "__main__":
  unittest.main()

