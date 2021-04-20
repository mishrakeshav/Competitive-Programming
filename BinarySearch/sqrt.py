"""
link : https://leetcode.com/problems/sqrtx/
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        def condition(val):
            return val*val > x 
        left,right = 0,x + 1 
        while left < right:
            mid = (left + right)//2 
            if condition(mid):
                right = mid 
            else:
                left = mid + 1 
        
        return left - 1 