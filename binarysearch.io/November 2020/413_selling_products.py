class Solution:
    def solve(self, items, n):
        freq = dict()
        for i in items:
            if i not in freq:
                freq[i] = 0 
            freq[i] += 1 
        
        counts = [freq[i] for i in freq]
        counts.sort()
        k = 0 
        for i in counts:
            if i <= n:
                k += 1 
                n -= i 
            else:
                break 
        return len(counts) - k 
                
        
        
                
        