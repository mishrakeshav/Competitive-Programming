class Solution:
    def solve(self,nums):
        max_1 = -float('inf')
        max_2 = max_1
        for num in nums:
            if num > max_1:
                max_2 = max_1
                max_1 = num 
            elif num > max_2:
                max_2 = num 
        m = max_1*max_2
        max_1 = float('inf')
        max_2 = float('inf')
        for num in nums:
            if num < max_1:
                max_2 = max_1
                max_1 = num 
            elif num < max_2:
                max_2 = num 
        m = max(m,max_1*max_2)
        return m
