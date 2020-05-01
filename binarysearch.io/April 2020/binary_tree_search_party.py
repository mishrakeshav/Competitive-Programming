# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def solve(self, root, val):
        # Write your code here
        def helper(root, val):
            if root is None:
                return False
            if root.val == val:
                return True
            return helper(root.left, val) or helper(root.right, val)
        return helper(root, val)
