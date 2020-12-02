class Solution:
    def solve(self, nums):
        n = len(nums)
        if n==0:
            return n 
        from collections import Counter
        freq = Counter(nums)
        
        l_max = [i for i in nums]
        r_min = [i for i in nums]
        
        for i in range(1,n):
            l_max[i] = max(l_max[i-1],l_max[i])
        
        for i in range(n-2,-1,-1):
            r_min[i] = min(r_min[i+1],r_min[i])
        
        ans = 0 
        for i in range(n):
            if freq[nums[i]]==1 and r_min[i]==l_max[i]==nums[i]:
                ans += 1 
        
        return ans 
            
        
        
        
        