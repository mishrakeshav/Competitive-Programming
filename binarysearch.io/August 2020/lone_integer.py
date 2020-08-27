"""
Problem Link:https://binarysearch.io/problems/Lone-Integer
Solution by Keshav Mishra 
"""
class Solution:
    def solve(self, nums):
        # Write your code here
        var = 0 
        nums.sort()
        flag = True 
        for i in range(1,len(nums)):
            if flag:
                if nums[i-1] != nums[i]:
                    var += nums[i-1] + nums[i]
                    flag = False 
            elif nums[i] != nums[i-1]:
                var += nums[i]
        s = 0 
        for num in nums:
            s += num 
        return (3*var - s)//2 
        
`
