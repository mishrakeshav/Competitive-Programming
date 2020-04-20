class Solution:
    def solve(self, arr):
        # Write your code here
        n = len(arr)
        a = 1
        
        for i in range(n):
            if arr[i] != a:
                return a
            a += 1
        return arr[-1] + 1
            
