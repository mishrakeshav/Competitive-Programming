class Solution:
    def solve(self, n):
        n1 = str(n)
        l = len(n1)
        s = 0 
        for i in n1:
            s += int(i)**l 
        return n == s 