# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root0, root1):
        # Write your code here
        def helper(node1,node2):
            if node1 is None and node2 is None:
                return True
            elif node1 is None:
                return False
            elif node2 is None:
                return False
            if node1.val !=node2.val:
                return False
            left = helper(node1.left,node2.left)
            right = helper(node1.right,node2.right)
            return left and right
        return helper(root0,root1)
