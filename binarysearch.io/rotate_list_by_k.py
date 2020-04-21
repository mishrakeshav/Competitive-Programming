class Solution:
    def solve(self, nums, k):
        # Write your code here
        n = len(nums)
        if k % n == 0:
            return nums
        else:
            if k > n:
                k = k//n
            while k:
                temp = nums[0]
                for i in range(1,n):
                    nums[i-1] = nums[i]
                nums[-1] = temp 
                k -=1
            return nums
                    
                    