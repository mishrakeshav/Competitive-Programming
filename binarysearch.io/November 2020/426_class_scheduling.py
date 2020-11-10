class Solution:
    def solve(self, times):
        times.sort(key = lambda x:x[1])
        ans = 0
        n = len(times)
        i = 0
        prev_end = -1
        while i < n:
            if prev_end < times[i][0]:
                prev_end = times[i][1]
                ans += 1 
            i += 1 
        if times[-1][0] > prev_end:
            ans += 1
        return max(ans,1)
            
        