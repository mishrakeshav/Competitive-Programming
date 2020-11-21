# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        # Write your code here
        siblings = []
        count = 0
        if root:
            siblings.append(root)
        while siblings:
            new = []
            for node in siblings:
                if node.left is None and node.right:
                    count += 1 
                if node.right is None and node.left:
                    count += 1 
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            siblings = new 
        
        return count
