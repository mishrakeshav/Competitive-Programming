"""
Problem Link:https://binarysearch.io/problems/Largest-Anagram-Group
"""
class Solution:
    def solve(self, words):
        # Write your code here
        counts =dict()
        for string in words:
            char = "".join(sorted(string))
            if char not in counts:
                counts[char] = 0 
            counts[char] += 1
        
        max_length = 0 
        for string in  counts:
            max_length = max(max_length, counts[string])
        return max_length

