class Solution:
    def solve(self, n):
        # Write your code here
        a = 1
        b = 1 
        if n <= 2:
            return 1
        else:
            for i in range(n-2):
                c = a + b
                a = b
                b = c
        return c
