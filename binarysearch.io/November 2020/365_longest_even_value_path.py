# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        def helper(root):
            if root is None:
                return 0,0,0
            x,y,z = helper(root.left)
            a,b,c = helper(root.right)
            k = 0 
            if root.val%2==0:
                k = max(x,y) + max(a,b) + 1
            k = max(z,c,k,x,y,a,b)
            x += 1 
            y += 1 
            a += 1 
            b += 1
            if root.val%2:
                x,y,a,b = 0,0,0,0
            return max(x,y) , max(a,b) ,k
        _,__,ans = helper(root)
        return ans
            
            
                
            
                
            
                
            
                
        