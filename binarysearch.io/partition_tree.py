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
                return 0,0
            
            if root.left is None and root.right is None:
                return 0,1
            
            internal1, leaves1 = helper(root.left)
            internal2 , leaves2 = helper(root.right)
            
            return internal1 + internal2 + 1, leaves1 + leaves2
        
        i,l =  helper(root)
        return l,i
            
        
