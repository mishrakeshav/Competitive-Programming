# dynamic programming 
class Solution:
    def solve(self, nums):
        n = len(nums)
        if n == 0:
            return n
        d = [1]*n
        for i in range(n):
            for j in range(i-1,-1,-1):
                if nums[j] < nums[i]:
                    d[i] = max(d[i],d[j]+1)
        return max(d) 

# recursive  
class Solution:
    def solve(self, nums):
        n = len(nums)
        if n == 0:
            return n 
        def helper(nums,i,prev,max_len):
            if i >= len(nums):
                return max_len 
            if nums[i] > prev:
                m1 = helper(nums,i+1,nums[i],max_len+1)
                m2 = helper(nums,i+1,prev,max_len)
                max_len = max(m1,m2)
            else:
                m1 = helper(nums,i+1,prev,max_len)
                max_len = max(max_len,m1)
            m3 = helper(nums,i+1,nums[i],1)
            max_len = max(max_len,m3)
            return max_len 
        return helper(nums,1,nums[0],1)
                

        
        
            
            
        
        