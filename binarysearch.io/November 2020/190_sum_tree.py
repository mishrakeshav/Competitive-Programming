# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        
        def helper(root):
            if root is None:
                return True 
            if root.left is None and root.right is None:
                return True 
            s = 0
            l = helper(root.left)
            r = helper(root.right)
            if root.left:
                s += root.left.val 
            if root.right:
                s += root.right.val
            return l and r and s == root.val
        return helper(root)