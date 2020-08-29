"""
Problem Link:https://binarysearch.io/problems/Longest-Anagram-Subsequence
"""
class Solution:
    def solve(self, a, b):
        # Write your code here
        c1 = dict()
        for char in a:
            if char not in c1:
                c1[char] = 0 
            c1[char] += 1 
        c2 = dict()
        for char in b:
            if char not in c2:
                c2[char] = 0 
            c2[char] += 1 
        max_len = 0 
        for char in c1:
            if char in c2:
                max_len += min(c1[char],c2[char])
        return max_len
