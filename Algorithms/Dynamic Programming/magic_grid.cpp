#include <bits/stdc++.h> 
using namespace std; 
int magic_grid_recursion(int ** input,int a, int b ,int n, int m){
    
    if(a == n && b == m){
        if(input[n][m] < 0) return abs(input[n][m]);
        return 1;
    }
    if(a > n || b > m){
        return 0;
    }

    int cost1 = input[a][b] + magic_grid_recursion(input,a + 1,b,n,m);
    int cost2 = input[a][b] + magic_grid_recursion(input,a,b + 1,n,m);
    if(cost1 != INT_MAX && cost2 != INT_MAX){
        if(cost1 < 0){
            cost1 = abs(cost1);
        }
        else if(cost2 < 0){
            cost2 = abs(cost2);
        }
        if(cost1 == 0){
            cost1 = 1;
        }
        if(cost2 == 0){
            cost2 = 1;
        }
        return min(cost1,cost2);
    }
    else if(cost1 !=INT_MAX){
        if(cost1 < 0){
            cost1 = abs(cost1);
        }
        if(cost1 == 0){
            cost1 = 1;
        }
        return cost1;
    }
    else if(cost2 != INT_MAX){
        if(cost2 < 0){
            cost2 = abs(cost2);
        }
        if(cost2 == 0){
            cost2 = 1;
        }
        return cost2;
    }
    // else{
    //     return 1;
    // }
}
void solve(); 
int main() 
{ 
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL); 
  
// #ifndef ONLINE_JUDGE 
//     freopen("input.txt", "r", stdin); 
//     freopen("error.txt", "w", stderr); 
//     freopen("output.txt", "w", stdout); 
// #endif 
  
    int t = 1; 
    cin >> t; 
    while (t--) { 
        
        solve(); 
        cout << "\n"; 
    
    } 
  
    // cerr << "time taken : " << (float)clock() / CLOCKS_PER_SEC << " secs" << endl; 
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
    for(int i = 0; i < n; i++){
        for(int j =0; j < m; j++){
            cin >> input[i][j];
        }
    }
    cin >> a >> b;
    // cout << "Hello World" << endl;
    int ans =  magic_grid_recursion(input,a,b,n-1,m-1);
    ans = 1;
    cout << ans << endl;
} 