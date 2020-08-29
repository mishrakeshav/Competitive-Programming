"""
Problem Link:https://binarysearch.io/problems/Steady-Car
"""
class Solution:
    def solve(self, positions):
        # Write your code here
        diff = 0 
        flag = True 
        m = 0 
        for i in range(1,len(positions)):
            if flag:
                diff = abs(positions[i]-positions[i-1])
                flag = False 
                count = 2 
            elif diff == abs(positions[i]-positions[i-1]):
                count += 1 
            else:
                diff = abs(positions[i]-positions[i-1])
                
                m = max(m,count)
                count = 2 
        m = max(m,count)
        return m
