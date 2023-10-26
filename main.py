class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def sum_of_depths(root: TreeNode, depth=0) -> int:
    if root is None:
        return 0

    depth_of_node = depth

    left_depth = sum_of_depths(root.left, depth + 1)
    right_depth = sum_of_depths(root.right, depth + 1)

    total_depth = depth_of_node + left_depth + right_depth

    return total_depth


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

result = sum_of_depths(root)
print(result)
