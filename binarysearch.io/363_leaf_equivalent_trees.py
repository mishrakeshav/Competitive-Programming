# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root1, root2):
        def inorder(root,level):
            if root is None:
                return 
            inorder(root.left,level)
            if root.left is None and root.right is None:
                level.append(root.val)
            inorder(root.right,level)
        level1 = []
        level2 = []
        inorder(root1,level1)
        inorder(root2,level2)
        
        return level1 == level2 
        
        
        