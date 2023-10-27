import unittest

from main import merge_intervals


class TestMergeIntervals(unittest.TestCase):
    def test1(self):

        intervals = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
        expected_result = [(0, 1), (3, 8), (9, 12)]
        result = merge_intervals(intervals)
        self.assertEqual(result, expected_result)

    def test2(self):

        intervals = []
        expected_result = []
        result = merge_intervals(intervals)
        self.assertEqual(result, expected_result)

    def test3(self):

        intervals = [(1, 5)]
        expected_result = [(1, 5)]
        result = merge_intervals(intervals)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
