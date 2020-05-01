# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        # Write your code here
        def cal(root):
            if root is None:
                return 0 
            else:
                return root.val + cal(root.left) + cal(root.right)
        
        return cal(root)
            
