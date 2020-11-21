"""
Given a list of integers nums, 
find the maximum product of integers in any contiguous sublist.
"""
class Solution:
    def solve(self, nums):
        # Write your code here
        
        max_p = 1
        lo = hi = 1
        for i in nums:
            lo, hi = min(lo*i, hi*i ,i), max(lo*i, hi*i ,i)
            max_p = max(max_p,hi)
        
        return max_p
        
            
