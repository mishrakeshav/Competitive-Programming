"""
Given a matrix of order n x m find the maximum sum path 
from (0,0) to (n-1,m-1)
"""
def solve_top_down():
    n, m = map(int,input().split())
    matrix = []
    for i in range(n):
        a = list(map(int,input().split()))
        matrix.append(a)

    dp = [[0 for i in range(m)] for j in range(n)]

    dp[-1][-1] = matrix[-1][-1]

    for i in range(m-2,-1,-1):
        dp[-1][i] = dp[-1][i+1] + matrix[-1][i]
    
    for i in range(n-2,-1,-1):
        dp[i][-1] = dp[i+1][-1] + matrix[i][-1]
    
    for i in range(n-2,-1,-1):
        for j in range(m-2,-1,-1):
            dp[i][j] = max(dp[i+1][j] , dp[i][j+1]) + matrix[i][j]
    
    print(dp[0][0])

    

def solve_bottom_up():
    n, m = map(int,input().split())
    matrix = []
    for i in range(n):
        a = list(map(int,input().split()))
        matrix.append(a)

    dp = [[0 for i in range(m)] for j in range(n)]
    dp[0][0] = matrix[0][0]

    for i in range(1,n):
        dp[i][0] = dp[i-1][0] + matrix[i][0]

    for i in range(1,m):
        dp[0][i] = dp[0][i-1] + matrix[0][i]
    
    for i in range(1,n):
        for j in range(1,m):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]


    print(dp[-1][-1])


if __name__ == '__main__':
    for t in range(int(input())):
        solve_top_down()