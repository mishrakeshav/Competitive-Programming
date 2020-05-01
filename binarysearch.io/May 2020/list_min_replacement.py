class Solution:
    def solve(self, nums):
        # Write your code here
        if len(nums) == 0:
            return nums
        s = nums[0]
        flag = True
        for i in range(1,len(nums)):
            if flag:
                k = nums[i]
                nums[i] = s
                if k < s:
                    s = k
                flag = False
            else:
                k = nums[i]
                nums[i] = s
                if k < s:
                    s = k
        nums[0] = 0
        return nums
                
            
