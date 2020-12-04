# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, a, b):
        if root is None:
            return -1
        left = self.solve(root.left,a,b)
        right = self.solve(root.right,a,b)
        if (root.val == a or root.val == b) and (left!=-1 or right!=-1):
            return root.val 
        
        if left!=-1 and right!=-1:
            return root.val
        
        if root.val==a or root.val==b:
            return root.val 
        
        if left!=-1: return left
        else: return right 
            
        
        
        
        
        
        