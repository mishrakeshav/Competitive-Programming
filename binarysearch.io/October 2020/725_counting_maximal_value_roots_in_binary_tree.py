# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        def helper(root):
            if root is None:
                return 0,-float('inf')
            if root.left is None and root.right is None:
                print(1,root.val)
                return 1,root.val
            
            c1,v1 = helper(root.left)
            c2,v2 = helper(root.right)
            count = c1 + c2 
            
            m = max(v1,v2,root.val)
            if m <= root.val:
                count += 1 
            print(count,root.val)
            return count,m 
        
        return helper(root)[0] 
