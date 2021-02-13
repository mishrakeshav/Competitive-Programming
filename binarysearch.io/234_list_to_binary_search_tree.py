# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, nums):
         
        def helper(nums):
            n = len(nums)
            if not n:
                return 
            newNode = Tree(nums[n//2])
            newNode.left = helper(nums[:n//2])
            newNode.right = helper(nums[n//2+1:])
            return newNode 
        return helper(nums)