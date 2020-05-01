class Solution:
    def solve(self, nums):
        # Write your code here
        
        count = dict()
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1 
        
        new_count = set()
        for i in count.values():
            if i not in new_count:
                new_count.add(i)
            else:
                return False
        return True
            
