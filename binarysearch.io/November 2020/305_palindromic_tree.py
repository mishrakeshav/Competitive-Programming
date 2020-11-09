# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        
        order = []
        def inorder(root):
            if root is None:
                return 
            inorder(root.left)
            order.append(root.val)
            inorder(root.right)
        inorder(root)
        return order == order[::-1]