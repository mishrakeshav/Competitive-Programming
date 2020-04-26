class Solution:
    def solve(self, s):
        # Write your code here
        for i in range(len(s)//2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True
