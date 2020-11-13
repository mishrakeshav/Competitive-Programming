class Solution:
    def solve(self, A):
        B = sorted(A,key = lambda x : x[1])
        A.sort()
        ans = left = INF = float('inf')
        j = 0 
        for s1,e1 in A:
            while j < len(A) and B[j][1] < s1:
                left = min(left,B[j][1]-B[j][0] + 1)
                j += 1 
            ans = min(ans,(e1-s1+1)+left)
        
        return ans if ans != INF else 0