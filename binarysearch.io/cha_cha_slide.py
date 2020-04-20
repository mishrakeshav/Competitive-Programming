class Solution:
    def solve(self, s1, s2):
        # Write your code here
        
        if len(s1) != len(s2):
            return False
        
        stack = ""
        i = 0
        while i < len(s1):
            if not(s1.startswith(s2[i:])):
                stack += s2[i]
            else:
                if s2[i:] + stack == s1:
                    return True 
                else:
                    return False
                    
            i += 1
                    
        return False
            
        
