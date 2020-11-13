# dp solution
class Solution:
    def solve(self, a, b):
        n = len(a)
        m = len(b)
        dp = dict()
        
        def helper(a,b,i,j,n,m):
            if (i,j) in dp:
                return dp[(i,j)]
            if i == n or j == m:
                return 0 
            if(a[i] == b[j]):
                dp[(i,j)] =  helper(a,b,i+1,j+1,n,m) + 1
                return dp[(i,j)]
            
            m1 = helper(a,b,i+1,j,n,m)
            m2 = helper(a,b,i,j+1,n,m)
            dp[(i,j)] = max(m1,m2)
            return dp[(i,j)]
        return helper(a,b,0,0,n,m)

# recursive solution
class Solution:
    def solve(self, a, b):
        n = len(a)
        m = len(b)
        def helper(a,b,i,j,n,m):
            if i == n or j == m:
                return 0 
            if(a[i] == b[j]):
                return helper(a,b,i+1,j+1,n,m) + 1
            m1 = helper(a,b,i+1,j,n,m)
            m2 = helper(a,b,i,j+1,n,m)
            return max(m1,m2)
        return helper(a,b,0,0,n,m)