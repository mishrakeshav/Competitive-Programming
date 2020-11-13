# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, preorder, inorder):
        if len(preorder)==0:
            return  
        root = Tree(preorder[0]) 
        s = set()
        s.add(preorder[0])
        i = 1 
        def helper(root,i):
            if root is None or i == len(preorder) or preorder[i] in s:
                return i 
            k2 = inorder.index(root.val)
            k1 = inorder.index(preorder[i])
            if k1 < k2:
                root.left = Tree(preorder[i])
                s.add(preorder[i])
                i += 1 
            i = helper(root.left,i)
            if i == len(preorder) or preorder[i] in s:
                return i 
            k1 = inorder.index(preorder[i])
            if k1 > k2:
                root.right = Tree(preorder[i])
                s.add(preorder[i])
                i += 1 
            i = helper(root.right,i)
            return i  
        helper(root,1)
        return root