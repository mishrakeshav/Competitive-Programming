class Solution:
    def solve(self, s, k):
        d = dict()
        
        n = len(s)
        for i in range(n-k +1):
            l = s[i:i+k]
            # print(l)
            if l not in d:
                d[l] = 0 
            d[l] += 1 
        ans = 0 
        for i in d:
            if d[i] >= 2:
                ans += 1 
        return ans