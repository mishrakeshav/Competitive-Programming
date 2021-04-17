class Solution:
    def solve(self, piles, k):
        piles.sort()
        mi = piles[0]
        mx = piles[-1]
        start,end = 1, mx
        ans = end
        def get_time(val):
            v = 0 
            for i in piles:
                
                v += (i + val - 1)//val
            return v 

        while start < end:
            mid = start + (end - start)//2 
            val = get_time(mid)
            if val <= k:
                ans = mid  
                end = mid 
            else:
                start = mid + 1 
        
        return ans 
        