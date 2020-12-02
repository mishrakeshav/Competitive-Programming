# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        total = 0
        def helper(root,s):
            nonlocal total 
            if root is None:
                return 
            s *= 10 
            s += root.val 
            if root.left is None and root.right is None:
                total += s  
            
            helper(root.left,s)
            helper(root.right,s)
            
            return total 
        
        return helper(root,0)
            
            
            
            
            
            
        
        
        