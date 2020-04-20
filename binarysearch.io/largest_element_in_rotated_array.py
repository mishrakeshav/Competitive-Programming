class Solution:
    def solve(self, arr):
        # Write your code here
        n = len(arr)
        
        if len(arr) == 1:
            return arr[0]
        
        for i in range(n-1):
            if arr[i+1] < arr[i]:
                return arr[i]
                
        return arr[-1]
        
            
            
            
            
            
