class Solution:
    def solve(self, nums):
        from collections import Counter
        freq = Counter(nums)
        for i in freq:
            if freq[i] == i:
                return True 
        return False