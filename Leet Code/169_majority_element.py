class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            if abs(nums[i]-i) > 1:
                return False 
        return True 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        count = 1 
        n = len(nums)
        if len(nums) == 1:
            return nums[-1]
        for i in range(1,n):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1 
            if count > n//2 :
                return nums[i]
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = 0 
        count = 1 
        n = len(nums)
        for i in range(n):
            if nums[majority] == nums[i]:
                count += 1 
            else:
                count -= 1 
            if count == 0:
                majority = i 
                count = 1 
        return nums[majority]

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def count_in_range(lo,hi,num):
            c = 0 
            for i in range(lo,hi+1):
                if num == nums[i]:
                    c += 1 
            return c 
        
        def helper(lo,hi):
            if lo==hi:
                return nums[lo]
            
            mid = (lo + hi)//2 
            left = helper(lo,mid)
            right = helper(mid + 1,hi)
            if left == right:
                return left 
            left_count = count_in_range(lo,mid,left)
            right_count = count_in_range(mid + 1,hi,right)
            if left_count > right_count:
                return left 
            return right 
        return helper(0,len(nums)-1)