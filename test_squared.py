import unittest

from main import sortedSquares


class TestSortedSquares(unittest.TestCase):
    def test1(self):
        nums = [-4, -2, 0, 1, 3]
        expected_result = [0, 1, 4, 9, 16]
        self.assertEqual(sortedSquares(nums), expected_result)

    def test2(self):
        nums = [1, 2, 3, 4, 5]
        expected_result = [1, 4, 9, 16, 25]
        self.assertEqual(sortedSquares(nums), expected_result)



if __name__ == "__main__":
    unittest.main()
