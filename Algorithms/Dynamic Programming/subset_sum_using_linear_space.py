"""
Given a set and a sum (m) findout whether 
there is a subset whose sub is equal to m

Time complexity : O(n*m)
Space complexity : O(n*m)
"""
def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [0 for i in range(m+1)]
    dp[0] = 1
    
    for i in range(n):
        for j in range(m+1):
            if (j - a[i]) >=0:
                if dp[j] == 0 and dp[(j - a[i])]:
                    dp[j] = a[i]
    
    if dp[m]:
        print(dp)
        print('YES')
        i = m 
        while i >= 1:
            print(dp[i], end = " ")
            i -= dp[i]
    else:
        print('NO')
    
        

            



if __name__ == '__main__':
    for t in range(int(input())):
        solve()