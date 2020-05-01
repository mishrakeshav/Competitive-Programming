from collections import Counter
class Solution:
    def solve(self, s):
        # Write your code here
        stack1 = []

        n = len(s)
        i = 0
        while i < n:
            if len(stack1):
                if stack1[-1] == s[i]:
                    stack1.pop()
                    k = s[i]
                    while k == s[i]:
                        i += 1
                    i -=1
                else:
                    stack1.append(s[i])
            else:
                stack1.append(s[i])
                    
            i += 1
        return "".join(stack1)
                
                
            
            
        
