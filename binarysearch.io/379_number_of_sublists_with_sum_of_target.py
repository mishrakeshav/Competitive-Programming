class Solution:
    def solve(self, nums, target):
        n = len(nums)
        if n == 0:
            return 0 
        prefix = [0]*n 
        prefix[0] = nums[0]
        
        for i in range(1,n):
            prefix[i] = nums[i] + prefix[i-1]
        count = 0 
        hashmap = dict()
        current = 0 
        for i in range(n):
            current += nums[i]
            if current == target:
                count += 1 
            if current-target in hashmap:
                count += hashmap[current-target] 
            if current in hashmap:
                hashmap[current] += 1 
            else:
                hashmap[current] = 1 
                
        return count 