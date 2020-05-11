class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = dict()
        s = 0
        count = 0
        for i in nums:
            s += i 
            if s == k:
                count += 1
            if s - k in prefix:
                count += 1
            if s not in prefix:
                prefix[s] = 0
            prefix[s] += 1
        return count
            
            
        
                
        
        