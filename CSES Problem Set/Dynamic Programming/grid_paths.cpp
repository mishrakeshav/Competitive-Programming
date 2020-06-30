#include <bits/stdc++.h> 
#include <string.h> 
using namespace std; 
int mod = 1e9 + 7;

int main(){
    int n;
    cin >>n;
    char ** grid = new char*[n];
    for(int i=0; i<n; i++){
        grid = new char[n];
    }
    for(int i =0; i < n; i++){
        for(int j=0; j < n; j++){
            cin >> grid[i][j];
        }
    }
    int dp[n][n];
    memset(dp,0,sizeof(dp));
    dp[n-1][n-1] = 1;
    
    return 0;
}