# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if root is None:
            return []
        level = []
        nodes = []
        nodes.append(root)
        while nodes:
            new = []
            for node in nodes:
                level.append(node.val)
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            nodes = new 
        return level 
        
