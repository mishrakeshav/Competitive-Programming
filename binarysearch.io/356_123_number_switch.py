class Solution:
    def solve(self, n):
        n = list(str(n))
        for i in range(len(n)):
            if n[i] != '3':
                n[i] = '3'
                break 
        
        return int(''.join(n))
                
        
        
        