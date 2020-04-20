class Solution:
    def solve(self, s):
        # Write your code here
        new_s = ""
        new_s += s[0]
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                new_s += s[i]
                
        return new_s
                
