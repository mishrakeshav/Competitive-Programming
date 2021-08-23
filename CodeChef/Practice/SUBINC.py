from math import ceil,floor, factorial as fact, inf 
from copy import deepcopy
def get_list():
    return list(map(int,input().split()))
def get_int():
    return int(input())

for t in range(get_int()):
    n = get_int()
    a = get_list()
    dp = [1 for i in range(n)]
    for i in range(1,n):
        if a[i] >= a[i-1]:
            dp[i] += dp[i-1]
    
    ans = sum(dp)
    print(ans)