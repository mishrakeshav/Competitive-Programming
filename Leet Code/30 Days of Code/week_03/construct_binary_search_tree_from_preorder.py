"""
Return the root node of a binary search tree that matches the given preorder traversal.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def insert_node(root,val):
            if root is None:
                return TreeNode(val)
            elif root.val > val:
                root.left = insert_node(root.left,val)
            elif root.val < val:
                root.right = insert_node(root.right,val)
            
            return root
        root = None
        for i in preorder:
            root = insert_node(root,i)
        
        return root