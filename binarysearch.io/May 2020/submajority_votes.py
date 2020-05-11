class Solution:
    def solve(self, nums):
        # Write your code here
        votes = [0]*(max(nums)+1)
        length = len(nums)
        for i in nums:
            votes[i] += 1
        r = []
        for n in range(len(votes)):
            if votes[n] > length//3:
                r.append(n)
            
        return r
                
