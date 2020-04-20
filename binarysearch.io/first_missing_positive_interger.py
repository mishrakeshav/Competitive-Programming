class Solution:
    def solve(self, nums):
        # Write your code here
        nums = sorted(nums)
        n = set()
        if len(nums) == 0:
            return 1
        
        for i in nums:
            n.add(i)
        if 1 not in n:
            return 1
        for i in nums:
            
            if i != 1 and i > 0:
                if i-1 not in n:
                    return i - 1
                elif i + 1 not in n:
                    return i + 1
        if len(nums) and nums[-1] > 0 :
            return nums[-1] + 1
        else:
            return 1
                