class Solution:
    def solve(self, nums):
        # Write your code here
        prefix = [1]*(len(nums))
        postfix = [1]*len(nums)
        prefix[0] = nums[0]
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]*nums[i]
        postfix[-1] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            postfix[i] = postfix[i+1]*nums[i]
        
        lst = []
        lst.append(postfix[1])
        
        for i in range(1,len(nums)-1):
            lst.append(prefix[i-1]*postfix[i+1])
        lst.append(prefix[-2])
        
        return lst
        
        
