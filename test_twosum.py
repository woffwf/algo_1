import unittest

from main import twoSum


class TestTwoSum(unittest.TestCase):
    def test_case_1(self):
        nums = [3, 6, 1, 8]
        target = 9
        expected_result = [[0, 1], [2, 3]]
        self.assertEqual(twoSum(nums, target), expected_result)

    def test_case_2(self):
        nums = [1, 2, 3, 4, 5]
        target = 9
        expected_result = [[3, 4]]
        self.assertEqual(twoSum(nums, target), expected_result)




if __name__ == "__main__":
    unittest.main()