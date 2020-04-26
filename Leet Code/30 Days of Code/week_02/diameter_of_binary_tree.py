# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        mx = 0
        def helper(root,mx):
            if root is None:
                return mx,0
            if root.left is None and root.right is None:
                return mx,1
            else:
                ml,l = helper(root.left,mx)
                mr,r = helper(root.right,mx)
                mx = max(ml,mr,l+r,mx)
                return mx,max(l+1,r+1)
        return helper(root,0)[0]
                
                
                
        
        
        
                
                
            
            
        