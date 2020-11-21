"""
Link : https://binarysearch.io/problems/The-Auditor
Solved by Keshav Mishra
"""
class Solution:
    def solve(self, s):
        # Write your code here
        n = len(s)
        ans = 0 
        for i in range(n):
            k = ord(s[n-i-1]) - ord('A') + 1
            ans += k*(26**(i))
        return ans
