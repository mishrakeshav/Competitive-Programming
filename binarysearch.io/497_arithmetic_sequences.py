class Solution:
    def solve(self, nums):
        
        ans = 0 
        if len(nums) <= 2:
            return 0 
        c = 0 
        for i in range(len(nums)-2):
            if (nums[i+2]-nums[i+1]) == (nums[i+1]-nums[i]):
                c += 1
            else:
                c = 0 
            ans += c 

        return ans 
        