"""
Given a list of strings lst and a list of integers p,
reorder lst so that every lst[i] gets placed to p[i].

Bonus: can you do it with O(1) space?
"""
class Solution:
    def solve(self, lst, p):
        # Write your code here
        
        sorted_arr = [x for _,x in sorted(zip(p,lst))]
        
        return sorted_arr
            
        
            
            
