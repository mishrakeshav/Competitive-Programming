"""
Link:https://binarysearch.io/problems/Leaves-in-Same-Level
Solution by Keshav Mishra
"""
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        # Write your code here
        if root is None:
            return True
        
        nodes = []
        nodes.append(root)
        found_leaf = False
        while nodes:
            new = []
            for node in nodes:
                if not node.left and not node.right:
                    found_leaf = True 
                    continue 
                if found_leaf and (node.left or node.right):
                    return False 
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            if found_leaf and len(new):
                return False
            nodes = new
        return True 
                    
