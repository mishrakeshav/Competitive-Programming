class Solution:
    def solve(self, n):
        def max_divide(a,b):
            while a%b==0:
                a //= b
            return a 
        n = max_divide(n,2)
        n = max_divide(n,3)
        n = max_divide(n,5)
        return n==1
            