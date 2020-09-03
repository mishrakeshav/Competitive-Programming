"""
Problem Link : https://binarysearch.io/problems/K-Compare
Solution by Keshav Mishra
"""
class Solution:
    def solve(self, a, b, k):
        n1 = len(a)
        n2 = len(b)
        if k == 0 and n1 > n2:
            return n1 
        
        b.sort(reverse = True)
        count = 0 
        for i in range(n1):
            c = 0 
            for j in range(k):
                if a[i] < b[j]:
                    c = 1 
                else:
                    c = 0 
                    break 
            count += c 
        return count


