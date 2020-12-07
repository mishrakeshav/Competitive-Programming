# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, preorder, inorder):
        pi = 0 
        n = len(preorder)
        def helper(i,j):
            nonlocal pi 
            if i > j:
                return 
            node = Tree(preorder[pi])
            pi += 1 
            for k in range(i,j+1):
                if inorder[k]==node.val:
                    node.left = helper(i,k-1)
                    node.right = helper(k+1,j)
                    break 
            return node 
        return helper(0,n-1)