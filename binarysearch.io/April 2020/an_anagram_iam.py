from collections import Counter
class Solution:
    def solve(self, s0, s1):
        # Write your code here
        s_1 = Counter(s1)
        s_0 = Counter(s0)
        return s_1==s_0
        
