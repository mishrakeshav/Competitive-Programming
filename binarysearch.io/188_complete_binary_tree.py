# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if root is None:
            return True 
        stack = [root,]
        
        while stack:
            new = []
            found = False 
            for node in stack:
                if found:
                    if node.left or node.right:
                        return False 
                if node.left is None:
                    found = True 
                if found and node.right:
                    return False 
                if node.right is None:
                    found = True 
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            stack = new 
        return True 
        
        