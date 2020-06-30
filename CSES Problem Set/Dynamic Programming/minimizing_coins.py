# def solve(n,coins,dp):
#     if n == 0:
#         return 0
#     if n < 0:
#         return float("inf")
#     if dp[n] != float("inf"):
#         return dp[n]
#     count = float("inf")
#     for coin in coins:
#         count = min(count,solve(n-coin,coins,dp) + 1)
#     dp[n] = count
#     return count

def solve_dp(x,coins):
    flag = True 
    for i in coins:
        if i == x:
            return 1
        elif i < x:
            flag = False 
    if flag:
        return -1

    dp = [float("inf") for i in range(x+2)]
    for i in coins:
        dp[i] = 1
        
    dp[0] = 0 
    for i in range(1,x+1):
        if dp[i] == float("inf"):
            count = float("inf")
            for coin in coins:
                if i - coin >= 0:
                    count = min(count,dp[i-coin] + 1)
            dp[i] = count 
    if dp[x] == float("inf"):
        return -1 
    return dp[x]
    
if __name__ == '__main__':
    n , x = map(int , input().split())
    coins  = list(map(int,input().split()))
    coins.sort()
    dp = [float("inf") for i in range(x+2)]
    print(solve_dp(x,coins))
    

    

