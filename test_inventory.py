import unittest
import inventory

class TestingInventory(unittest.TestCase):
    def test_slotlimit(self):
        self.assertEqual(inventory.slotCount,9)

if __name__ == '__main__':
    unittest.main()
    
