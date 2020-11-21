class Solution:
    def solve(self, s0, s1):
        # Write your code here
        new_str = ""
        n = min(len(s0),len(s1))
        for i in range(n):
            new_str += s0[i] + s1[i]
        if len(s0) == n:
            new_str += s1[n:]
        elif len(s1) == n:
            new_str += s0[n:]
        return new_str