"""
You are given a list of flights that were taken, 
represented as origin to destination airport pairs. Given that this list was shuffled, 
find all the airports that were visited in the correct order.

Note: you can assume that no airport was visited twice.

Input:
s = [["WRE", "RPM"],
["AGN", "WRE"],
["NTL", "AGN"]]

Output:
["NTL", "AGN", "WRE", "RPM"]
"""
class Solution:
    def solve(self, s):
        # Write your code here
        k = dict()
        v = set()
        
        for key,value in s:
            k[key] = value
            v.add(value)
        start = None
        for i in k:
            if i not in v:
                start = i 
                break 
        
        new_list = []
        while start:
            new_list.append(start)
            start = k.get(start,None)
        
        return new_list
                
        
        
            
