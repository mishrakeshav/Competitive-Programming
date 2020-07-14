"""
Given a set and a sum (m) findout whether 
there is a subset whose sub is equal to m

Time complexity : O(n*m)
Space complexity : O(n*m)
"""
def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(m+1):
        dp[0][i] = 0
    for i in range(n+1):
        dp[i][0] = 1
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if dp[i-1][j]:
                dp[i][j] = 1 
            else:
                if ((j-a[i-1]) >= 0):
                    dp[i][j] = dp[i][(j-a[i-1])]  
    if dp[i][j]:
        print('YES')
    else:
        print('NO') 



if __name__ == '__main__':
    for t in range(int(input())):
        solve()