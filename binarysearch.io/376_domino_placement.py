class Solution:
    def solve(self, n, m):
        if n%2==0:
            return m*(n//2) 
        if m%2==0:
            return n*(m//2)
        
        return ((n-1)//2)*m + (m-1)//2 