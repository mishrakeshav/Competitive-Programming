# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def helper(root):
            if root is None:
                return 0,0
            if root.left is None and root.right is None:
                return 1,1 
            l1,m1 = helper(root.left)
            l2,m2 = helper(root.right)
            l = max(l1,l2) + 1 
            m = max(l1 + l2 + 1, m1 ,m2)
            
            return l,m
        l,m = helper(root)
        if m:
            return m -1 
        return m
        