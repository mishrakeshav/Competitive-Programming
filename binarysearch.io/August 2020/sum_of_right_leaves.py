"""
Problem Link: https://binarysearch.io/problems/Sum-of-right-leaves
"""
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        # Write your code here
        def helper(node):
            if node is None:
                return 0 
            count = 0 
            if node.right:
                if node.right.left is None and node.right.right is None:
                    count += node.right.val 
                else:
                    count += helper(node.right)
            
            if node.left:
                count += helper(node.left)
            return count 
        
        return helper(root)
