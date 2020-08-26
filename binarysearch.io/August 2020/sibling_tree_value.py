# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, k):
        # Write your code here
        def solve(node,parent,dr):
            if node is None:
                return 
            
            if node.val == k:
                if dr == 'left':
                    return parent.left.val  
                else:
                    return parent.right.val 
            
            val = solve(node.left, node, 'right')
            if val is not None:
                return val 
            val = solve(node.right, node, 'left')
            if val is not None:
                return val 
        
        return solve(root, None, None)
            
            
        
            
