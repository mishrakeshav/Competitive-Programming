# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Given the root of a binary tree, find the most frequent subtree sum.
The subtree sum of a node is the sum of all values under a node, including the node itself.
"""

class Solution:
    def solve(self, root):
        # Write your code here
        f = dict()

        def helper(root, f):
            if root is None:
                return 0
            s = root.val
            s += helper(root.left, f)
            s += helper(root.right, f)
            if s in f:
                f[s] += 1
            else:
                f[s] = 1
            return s
        helper(root, f)
        m = -1
        n = -1
        for i in f:
            if f[i] > m:
                m = f[i]
                n = i
        return n
