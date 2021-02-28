# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):


        def helper(root):
            if root is None:
                return None 
            root.left = helper(root.left)
            root.right = helper(root.right)

            if root.left is None and root.right is None:
                if root.val%2==0:
                    return None 
            return root
        return helper(root)
            