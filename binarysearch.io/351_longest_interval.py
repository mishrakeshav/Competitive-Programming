class Solution:
    def solve(self, intervals):
        intervals.sort()

        preva,prevb = 0,0
        max_interval = 0 
        inta,intb = 0,0
        for a,b in intervals:
            if a <= prevb:
                prevb = max(b,prevb)
                max_interval = max(prevb - preva + 1,max_interval)
            else:
                preva = a 
                prevb = b 
        max_interval = max(max_interval,prevb-preva+1)
        return max_interval