#include <bits/stdc++.h> 
using namespace std; 
/*
You are given a grid of size m, n. 
You have to find out the minimum amount of points required at the starting point. 
to reach from a, b to n , m in the grid. 
The numbers of the grid can be negative. 
The number of points at any index cannot be zero or negative
Input : 
1
3 3
-10 -1 -2
5 -10 -3
-20 -10 -1
0 0

Output: 
18
18 8 7 
10 15 5 
32 12 2 
0 0
18
18 8 7 
10 15 5 
32 12 2 


*/
int magic_grid_dp(int ** input, int a, int b, int n, int m, int ** output){
    if(input[n][m] > 0) output[n][m] = 0;
    else output[n][m] = abs(input[n][m]) + 1;

    for(int i = n-1 ; i >= 0 ; i-- ){
        if(input[i][m] > 0){
            if(input[i][m] >= output[i + 1][m]){
                output[i][m] = 1;
            }
            else{
                output[i][m] = output[i + 1][m] - input[i][m];
            }
            
        }else{
            output[i][m] = output[i + 1][m] + abs(input[i][m]);
        } 
    } 
    for(int i = m - 1;i >= 0; i--){
        if(input[n][i] > 0){
            if(input[n][i] >= output[n][i + 1]){
                output[n][i] = input[n][i] - output[n][i + 1];
            }
            else{
                output[n][i] = output[n][i + 1]- input[n][i];
            }
            
        } 
        else {
            output[n][i] = output[n][i+ 1] + abs(input[n][i]) ;
        }
    }
    int cost;
    for(int i = n - 1; i >= 0; i--){
        for(int j = m - 1; j >= 0; j--){
            cost = min(output[i + 1][j] , output[i][j + 1]);
            if(input[i][j] > 0){
                if(input[i][j] >= cost){
                    output[i][j] = 1;
                }
                else{
                    output[i][j] = cost - input[i][j];
                }
                
            } 
            else{
                output[i][j] = cost + abs(input[i][j]);
            } 
        }
    }
    
    return output[a][b];
}
int magic_grid_recursion(int ** input,int a, int b ,int n, int m , int ** output){
    
    if(a == n && b == m){
        if (input[n][m] > 0) output[n][m] = 1;
        else output[n][m] = abs(input[n][m]) + 1;
        return output[n][m];
    }
    if(a < n and b < n){
        int cost1 = magic_grid_recursion(input,a + 1,b,n,m, output);
        int cost2 = magic_grid_recursion(input, a, b + 1, n , m,output);
        if(input[a][b] > 0){
            if(input[a][b] > cost1){
                cost1 = 1;
            }
            else{
                cost1 -= input[a][b];
            }
            if(input[a][b] > cost2){
                cost2 = 1;
            }
            else{
                cost2 -= input[a][b];
            }
        }
        else{
            cost1 += abs(input[a][b]);
            cost2 += abs(input[a][b]);
        }
        output[a][b] = min(cost1,cost2);
        return min(cost1,cost2);
    }
    else{
        int cost;
        if(a == n){
            cost = magic_grid_recursion(input,a,b+1,n,m,output);
        }
        if(b == m){
            cost = magic_grid_recursion(input,a + 1,b, n ,m, output);
            
        }
        if(input[a][b] > 0){
            if(input[a][b] > cost){
                cost = 1;
            }
            else{
                cost -= input[a][b] ;
            }

        }
        else{
            cost += abs(input[a][b]);
        }
        output[a][b] = cost;
        return cost;
    }

}
void solve(); 
int main() 
{ 
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL); 
  
#ifndef ONLINE_JUDGE 
    freopen("input.txt", "r", stdin); 
    freopen("error.txt", "w", stderr); 
    freopen("output.txt", "w", stdout); 
#endif 
  
    int t = 1; 
    cin >> t; 
    while (t--) { 
        
        solve(); 
        cout << "\n"; 
    
    } 
  
    cerr << "time taken : " << (float)clock() / CLOCKS_PER_SEC << " secs" << endl; 
    return 0; 
} 
void solve() 
{ 
    int n , m, a, b;
    cin >> n >> m;
    int ** input = new int*[n];
    for(int i=0; i<n;i++){
        input[i] = new int[m];
    }
    int ** output = new int*[n];
    for(int i=0; i<n;i++){
        output[i] = new int[m];
    }
    for(int i = 0; i < n; i++){
        for(int j =0; j < m; j++){
            cin >> input[i][j];
        }
    }
    cin >> a >> b;
    
    int ans =  magic_grid_recursion(input,a,b,n-1,m-1, output);
    // ans = 1;
    cout << ans << endl;
    for(int i = 0; i < n; i++){
        for(int j = 0 ; j < m; j++){
            cout << output[i][j] << " ";
        }
        cout << "\n";
    }
    cout << a << " " << b << endl;
    int ** dp = new int*[n];
    for(int i=0; i<n;i++){
        dp[i] = new int[m];
    }
    ans = magic_grid_dp(input, a, b, n-1 , m-1 , dp);
    cout << ans << endl;
    for(int i = 0; i < n; i++){
        for(int j = 0 ; j < m; j++){
            cout << dp[i][j] << " ";
        }
        cout << "\n";
    }


} 