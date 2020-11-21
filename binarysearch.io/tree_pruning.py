# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def solve(self, root):
        # Write your code here

        def helper(root):
            if root is None:
                return

            if root.left is None and root.right is None:
                if root.val == 0:
                    return None
                else:
                    return root
            root.left = helper(root.left)
            root.right = helper(root.right)
            if root.left or root.right:
                return root
            else:
                if root.val == 1:
                    return root
                else:
                    return None
        return helper(root)
