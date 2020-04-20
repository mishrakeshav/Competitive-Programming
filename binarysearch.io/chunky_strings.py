class Solution:
    def solve(self, s, n):
        # Write your code here
        strings = []
        c = 0
        st = ""
        for i in range(len(s)):
            
            
            if c == n:
                strings.append(st)
                st = ""
                c = 0
            
            st += s[i]
            c += 1
        if c > 0:
            strings.append(st)
        return strings
            
