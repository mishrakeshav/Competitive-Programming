from copy import deepcopy
from math import floor,ceil,inf
def get_list():
    return list(map(int,input().split()))
def get_int():
    return int(input())

for t in range(get_int()):
    n,k = get_list()
    a = get_list()
    prefix = [[-inf for i in range(k+1)] for i in range(n+1)]
    dp = [[-inf for i in range(k+1)] for i in range(n+1)]
    for i in range(n):
        dp[i][0] = 0 
        prefix[i][0] = 0 
        for j in range(1,k+1):
            dp[i][j] = -inf 
            prefix[i][j] = -inf 
    dp[0][1] = a[0]
    prefix[0][1] = dp[0][1]
    for i in range(1,n):
        for j in range(1,k+1):
            dp[i][j] = max(prefix[i-1][j-1],dp[i-1][j]) + + j*a[i]
            dp[i][j] = max(dp[i][j],-inf)
            prefix[i][j] = max(prefix[i-1][j],dp[i][j])
    ans = -inf 
    for i in range(n):
        ans = max(ans,dp[i][k])
    print(ans)
