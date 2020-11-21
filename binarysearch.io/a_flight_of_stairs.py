class Solution:
    def solve(self, n):
        # Write your code here
        a = 1
        b = 1
        if n == 1:
            return a
        elif n==2:
            return a+b
        for i in range(n-1):
            c = a+b
            a = b
            b = c
        return c
            