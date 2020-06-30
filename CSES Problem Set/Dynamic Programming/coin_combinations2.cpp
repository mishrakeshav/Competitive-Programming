#include <bits/stdc++.h> 
using namespace std; 
int mod = 1e9 + 7;
int coin_combination2(int n, int amount, int * coins){
    int dp[n + 1][amount + 1];
    memset(dp,0,sizeof(dp));
    dp[0][0] = 1;
    for(int i = 1; i <= n; i++){
        for(int j = 0; j <= amount; j++){
            dp[i][j] = dp[i-1][j];
            if(j - coins[i-1] >= 0){
                dp[i][j] = (dp[i][j] + dp[i][j - coins[i-1]])%mod;
            }
        }
    }
    return dp[n][amount];

}
int coin_combinations(int n, int amount, int *coins, int ** dp){
    if(n == 0){
        return 0;
    }
    if(amount < 0){
        return 0;
    }
    if(amount == 0){
        return 1;
    }
    if(dp[amount][n] != -1){
        return dp[amount][n];
    }
    int first = coin_combinations(n,amount-coins[0],coins, dp)%mod ;
    int second = coin_combinations(n-1,amount,coins+1, dp)%mod ;
    dp[amount][n] = (first%mod + second%mod)%mod;
    return dp[amount][n];
}   
int main() 
{ 
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL); 
  
#ifndef ONLINE_JUDGE 
    freopen("input.txt", "r", stdin); 
    freopen("error.txt", "w", stderr); 
    freopen("output.txt", "w", stdout); 
#endif   
    int n , amount ;
    cin >> n >> amount;
    int * coins = new int[n];
    for(int i=0; i < n; i++){
        cin >> coins[i];
    }
    int ** dp = new int*[amount+1];
    for(int i=0; i<= amount; i++){
        dp[i] = new int[n+1];
    }
    for(int i=0; i<= amount; i++){
        for(int j= 0; j<=n; j++){
            dp[i][j] = -1;
        }
    }

    int ans = coin_combination2(n,amount,coins);
    cout << ans << endl;
    cerr << "time taken : " << (float)clock() / CLOCKS_PER_SEC << " secs" << endl; 
    return 0; 
} 
