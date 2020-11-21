"""
Problem Link: https://binarysearch.io/problems/Stack-Sequence
Solution by Keshav Mishra
"""
class Solution:
    def solve(self, pushes, pops):
        # Write your code here
        n1 = len(pushes)
        n2 = len(pops)
        i = 0 
        j = 0 
        stack = []
        while i < n1 and j < n2:
            stack.append(pushes[i])
            while len(stack) and j < n2 and stack[-1] == pops[j]:
                j += 1 
                stack.pop()
            i += 1 
        while len(stack) and j < n2 and stack[-1] == pops[j]:
            j += 1 
            stack.pop()
        
        return j == n2 