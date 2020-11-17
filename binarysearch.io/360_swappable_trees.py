# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root1, root2):
        def helper(root1,root2,is_swaped=False ):
            if root1 and not root2:
                return False 
            if root2 and not root1:
                return False 
            if not root1 and not root2:
                return True 
            if root1.val != root2.val:
                return False 
            ans1 = helper(root1.left,root2.left)
            ans2 = helper(root1.right,root2.right)
            if ans1 and ans2:
                return True 
            ans3 = helper(root1.left,root2.right)
            ans4 = helper(root1.right,root2.left)
            
            return ans3 and ans4
        
        return helper(root1,root2) 