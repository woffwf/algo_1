
import unittest

from src.main import max_experience


class TestMaxExperience(unittest.TestCase):

    def test_max_experience_example(self):
        L = 3
        experience = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = max_experience(L, experience)
        self.assertEqual(result, 1)



if __name__ == '__main__':
    unittest.main()
