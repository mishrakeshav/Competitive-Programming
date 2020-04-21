class Solution:
    def solve(self, n):
        # Write your code here
        l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'
            , 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
            'X', 'Y', 'Z'
        ]
        s = ""
        
        while n > 26:
            j = n%26
            n = n//26
            s += l[j-1]
        if n <= 26:
            s += l[n-1]
        
        return s[::-1]
            
            
            
        
