class Solution:
    def solve(self, nums):
        # Write your code here
        k = dict()
        j = 0
        new_nums = []
        for i in nums:
            if i not in k:
                k[i] = 0
            k[i] += 1
        
        for i in nums:
            if k[i] == 1:
                new_nums.append(i)
                
        return new_nums
                
                
                
                
                
