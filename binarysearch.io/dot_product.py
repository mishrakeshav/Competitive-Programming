class Solution:
    def solve(self, a, b):
        # Write your code here
        n = min(len(a), len(b))
        p = 0
        for i in range(n):
            p += a[i]*b[i]
        return p
            
