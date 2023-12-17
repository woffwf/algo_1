import unittest

from src.main import boyer_moore_search


class TestBoyerMooreSearch(unittest.TestCase):

    def test_boyer_moore_search_found(self):
        haystack = "ababcababcabcabc"
        needle = "abcabc"
        result = boyer_moore_search(haystack, needle)
        expected_result = 7

        self.assertEqual(result, expected_result)

    def test_boyer_moore_search_not_found(self):
        haystack = "ababcababcabcabc"
        needle = "xyz"
        result = boyer_moore_search(haystack, needle)
        expected_result = -1

        self.assertEqual(result, expected_result)

    def test_boyer_moore_search_empty_needle(self):
        haystack = "ababcababcabcabc"
        needle = ""
        result = boyer_moore_search(haystack, needle)
        expected_result = 0

        self.assertEqual(result, expected_result)

    def test_boyer_moore_search_empty_haystack(self):
        haystack = ""
        needle = "abcabc"
        result = boyer_moore_search(haystack, needle)
        expected_result = -1

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
