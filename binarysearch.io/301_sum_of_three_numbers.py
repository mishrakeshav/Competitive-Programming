class Solution:
    def solve(self, nums, k):
        n = len(nums)
        nums.sort()
        for i in range(n):
            target = k - nums[i]
            k1 = i + 1
            k2 = n - 1 
            while k1 < k2:
                if (nums[k1] + nums[k2]) == target:
                    return True 
                elif (nums[k1] + nums[k2]) > target:
                    k2 -= 1 
                else:
                    k1 += 1 
        return False
                
                
                
                
        