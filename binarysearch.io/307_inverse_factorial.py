class Solution:
    def solve(self, a):
        n = a 
        k = 0
        while n!=1:
            k += 1
            if n%k:
                return -1 
            n //=k 
        return k if k else 1  