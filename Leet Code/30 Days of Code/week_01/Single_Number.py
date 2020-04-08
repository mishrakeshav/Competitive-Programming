#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3283/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number = nums[0]
        for i in range(1,len(nums)):
            number ^= nums[i]
        return number
            

s = Solution()
print(s.singleNumber([2,2,1]))