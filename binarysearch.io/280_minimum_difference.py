class Solution:
    def solve(self, lst1, lst2):
        lst1.sort()
        lst2.sort()
        n = len(lst1)-1
        m = len(lst2)-1
        
        i = 0 
        j = 0
        ans = float('inf')
        while i <= n and j <= m:
            ans = min(abs(lst1[i]-lst2[j]),ans)
            if lst1[i] < lst2[j]:
                i += 1 
            elif lst1[i] > lst2[j]:
                j += 1 
            else:
                return ans 
        return ans 
            
        
        