# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Given a binary search tree root, and integers lo and hi, 
return the count of all nodes in root whose values are between lo and hi (inclusive).

For example, with this tree and lo=5 and hi=10, return 3 since only 7, 8, 9 are between [5, 10].
"""



class Solution:
    def solve(self, root, lo, hi):
        # Write your code here
        
        def helper(root,lo,hi,count):
            if root is None:
                return count
            
            if root.val >= lo and root.val <= hi:
                count += 1
            
                
            if root.left:
                count += helper(root.left,lo,hi,0)
            
            if root.right:
                
                count  += helper(root.right,lo,hi,0)

            
            return count
        return helper(root,lo,hi,0)
