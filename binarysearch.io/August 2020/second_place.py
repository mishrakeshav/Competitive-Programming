"""
Problem Link: https://binarysearch.io/problems/Second-Place
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
            return None 
        nodes = []
        nodes.append(root)
        count = 0 
        prev = 0 
        now = 0
        while nodes:
            new = []
            flag = True 
            for node in nodes:
                if flag and (not node.left) and (not node.right):
                    prev = now 
                    now = count 
                    flag = False
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            nodes = new 
            count += 1 
        return prev 
