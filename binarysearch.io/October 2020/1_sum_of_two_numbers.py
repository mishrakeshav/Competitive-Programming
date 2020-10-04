class Solution:
    def solve(self,nums,k):
        hashmap = dict()
        for num in nums:
            if k - num in hashmap:
                return True
            hashmap[num] = 1 
        return False 
