# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        # Write your code here
        l = []
        def helper(root,l):
            if root is None:
                return
            helper(root.left,l)
            l.append(root.val)
            helper(root.right,l)
        helper(root,l)
        return l
        
        
