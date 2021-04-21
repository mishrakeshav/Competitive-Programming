"""
link : https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
"""
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def condition(val):
            c = 0 
            ajk = 0 
            for i in bloomDay:
                if i - val <= 0:
                    ajk += 1 
                else:
                    ajk = 0
                if ajk == k:
                    c += 1 
                    ajk = 0 
            return c >= m
        if len(bloomDay) < m*k:
            return -1 
        left,right =  min(bloomDay) , max(bloomDay)
        
        while left < right:
            mid = (left + right)//2 
            if condition(mid):
                right = mid 
            else:
                left = mid + 1 
            
        return left 
	Keshav Mishra	TE																			
33
Jaideep More	TE																		
34
Prachiti Gholap	SE																		
35
Revaa Naik	BE