# test subhashkumar_module1_1_addnums.py
# This file contains test cases for the addnum function.

import unittest

# Import the functions that we want to test.
from subhashkumar_module1_1_addnums import add


class TestAddNums(unittest.TestCase):
    # Test the add function.
    def test_add(self):
        self.assertEqual(add(10, 5), 15)

# Run all tests when this file is executed directly.
if __name__ == "__main__":
    unittest.main()