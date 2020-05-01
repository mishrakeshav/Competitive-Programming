# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        # Write your code here
        def helper(root,c,s):
            if root is None:
                return 0,0
            s += root.val 
            c += 1
            lc,ls = helper(root.left, 0, 0)
            rc, rs = helper(root.right, 0, 0)
            
            if lc == rc:
                if ls > rs:
                    return c + lc,s + ls
                else:
                    return c + rc , s + rs
            elif lc > rc:
                return c + lc,s + ls
            else:
                return c + rc , s + rs
        _ , s = helper(root,0,0)
        return s
        
