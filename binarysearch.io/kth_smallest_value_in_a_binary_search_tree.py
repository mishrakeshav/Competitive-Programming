# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def solve(self, root, k):
        # Write your code here
        i = []

        def inorder(root, l):
            if root is None:
                return

            inorder(root.left, l)
            l.append(root.val)
            inorder(root.right, l)

        inorder(root, i)
        return i[k]
