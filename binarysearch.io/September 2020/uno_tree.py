"""
Problem Link: https://binarysearch.io/problems/Uno-Tree
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
        flag = True
        val = root.val 
        nodes.append(root)
        while nodes:
            newNodes = []
            for node in nodes:
                if node.val != val:
                    return False
                    break
                if node.left:
                    newNodes.append(node.left)
                if node.right:
                    newNodes.append(node.right)
            nodes = newNodes
                
        return True 
