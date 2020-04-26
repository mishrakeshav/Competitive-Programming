# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        # Write your code here
        def inorder(root,l):
            if root is None:
                return
            inorder(root.left,l)
            l.append(root.val)
            inorder(root.right,l)
        l = []
        inorder(root,l)
        return l == sorted(l)
        
            
            
                
                
            
                
            
                
            
            
