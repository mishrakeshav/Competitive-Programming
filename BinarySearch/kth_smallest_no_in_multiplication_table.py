class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def condition(val):
            c = 0 
            for i in range(1,m+1):
                add = min(val//i,n)
                if add:
                    c += add 
                else:
                    break 
            return c >= k 
                
        
        left,right = 1,m*n 
        while left < right:
            mid = left + (right - left)//2 
            if condition(mid):
                right = mid 
            else:
                left = mid + 1 
        
        return left 