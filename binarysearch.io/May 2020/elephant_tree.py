# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        # Write your code here
        def helper(root,s):
            if root is None:
                return 0 
            if root.left is None and root.right is None:
                return root.val 
            
            left = helper(root.left,0)
            right = helper(root.right,0)
            s = left + right
            
            root.val += s
            
            return root.val
        
        helper(root,0)
        return root