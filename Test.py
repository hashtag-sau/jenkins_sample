import unittest

from Addition.py import add

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        data = [20, 36]
        result = add(data)
        self.assertEqual(result, 56)

if __name__ == '__main__':
    unittest.main()
