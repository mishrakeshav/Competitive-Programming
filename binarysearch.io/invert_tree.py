# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def solve(self, root):
        # Write your code here
        def helper(root):
            if root is None:
                return None

            left = root.left
            right = root.right
            root.left = right
            root.right = left
            if root.left:
                helper(root.left)
            if root.right:
                helper(root.right)

            return root
        return helper(root)
