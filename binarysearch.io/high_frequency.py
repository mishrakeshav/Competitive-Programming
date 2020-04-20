class Solution:
    def solve(self, nums):
        # Write your code here
        count = dict()
        for i in nums:
            if i in count:
                count[i] += 1 
            else:
                count[i] = 1 
        value = None 
        c = 0
        
        for i in count:
            if count[i] > c:
                value = i 
                c = count[i]
        return c
