class Solution:
    def solve(self, num):
        # Write your code here
        data = num
        
        s = 0
        while data:
            s += data%10
            data = data//10
        return s