"""
Problem Link:https://binarysearch.io/problems/Palindromic-Anagram
Solution by Keshav Mishra
"""
class Solution:
    def solve(self, s):
        # Write your code here
        from collections import Counter
        freq = Counter(s)
        flag = 0
        for key in freq:
            if freq[key]%2:
                flag += 1 
        if flag > 1:
            return False 
        return True 

