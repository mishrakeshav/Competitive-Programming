class Solution:
    def solve(self, s1, s2):
        # Write your code here
        i = 0
        if s1 == "":
            return True
        if s1 == s2:
            return True
        final = len(s1)-1
        for s in s2:
            if s == s1[i]:
                i += 1
            
            if i == final:
                return True
        return False
                
            