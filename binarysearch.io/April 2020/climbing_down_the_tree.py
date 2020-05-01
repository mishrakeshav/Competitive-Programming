# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Given the root to a binary tree, return the largest sum of any path that goes from the root to a leaf.
"""
class Solution:
    def solve(self, root):
        # Write your code here
        def helper(root,s):
            if root is None:
                return 0

            s += root.val
            left = helper(root.left ,0)
            right = helper(root.right,0)

            if left >= right:
                s += left
            else:
                s += right
            return s
        return helper(root,0)

