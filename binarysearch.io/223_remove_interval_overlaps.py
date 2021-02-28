class Solution:
    def solve(self, intervals):
        intervals.sort(key = lambda x : x[1])
        ans = 0 
        pa,pb = None,None
        for a,b in intervals:
            if pa is None:
                pa = a 
                pb = b 
            elif pb > a:
                ans += 1 
            else:
                pb = b 
                pa = a 
        return ans 