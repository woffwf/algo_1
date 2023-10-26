from main import TreeNode, sum_of_depths

import unittest


class TestSumOfDepths(unittest.TestCase):
    def test_sum_of_depths(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)


        expected_result = 10


        result = sum_of_depths(root)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
