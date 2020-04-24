# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        # Write your code here
        s = ""
        def evaluate(root):
            
            if root.left is None and root.right is None:
                return int(root.val)
            else:
                left = evaluate(root.left)
                right = evaluate(root.right)
                
            
            return eval(str(left) + root.val + str(right))
            
            
            
        
        return evaluate(root)