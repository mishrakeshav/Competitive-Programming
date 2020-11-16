class Solution:
    def solve(self, intervals, point):
        ans = 0 
        for x,y in intervals:
            if x<=point<=y:
                ans += 1 
        return ans