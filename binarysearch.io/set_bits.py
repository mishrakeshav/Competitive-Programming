class Solution:
    def solve(self, n):
        # Write your code here
        count = 0
        for i in range(1,n+1):
            temp = i
            while temp:
                if temp&1:
                    count += 1
                temp >>=1
        return count
            
