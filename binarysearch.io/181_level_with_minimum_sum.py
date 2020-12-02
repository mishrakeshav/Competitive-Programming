# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        
        stack = []
        stack.append(root)
        level = -1
        min_sum = float('inf')
        l = 0 
        while stack:
            new = []
            s = 0 
            for node in stack:
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
                s += node.val 
            
            if s < min_sum:
                level = l 
                min_sum = s 
            l += 1 
            stack = new
        
        return level 
                
        