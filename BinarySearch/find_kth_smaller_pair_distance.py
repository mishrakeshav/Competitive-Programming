class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def condition(val):
            count,i,j = 0,0,0
            n = len(nums)
            while i < n or j < n:
                while j < n and nums[j] - nums[i] <= val:
                    j += 1 
                count += j - i - 1 
                i += 1 
            return count >= k
        
        left,right = 0,max(nums)
        nums.sort()
        while left < right:
            mid = left + (right - left)//2 
            if condition(mid):
                right = mid 
            else:
                left = mid + 1 
        
        return left 