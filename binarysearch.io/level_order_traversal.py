# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        # Write your code here
        
        def helper(root):
            waiting = []
            waiting.append(root)
            r = []
            while waiting:
                new_waiting = []
                for node in waiting:
                    r.append(node.val)
                    if node.left:
                        new_waiting.append(node.left)
                        
                    if node.right:
                        new_waiting.append(node.right)
                    
                waiting = new_waiting
            return r
        return helper(root)
                    
                        
            
