"""
link : https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
"""
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def condition(val):
            c = 1
            r = val
            for i in weights:
                if r >= i :
                    r -= i  
                else:
                    c += 1 
                    r = val  
                    r -= i 
            return c <= D 
        left,right = max(weights),sum(weights)
        
        while left < right:
            mid = (left + right)//2 
            if condition(mid):
                right = mid 
            else:
                left = mid + 1 
        return left 