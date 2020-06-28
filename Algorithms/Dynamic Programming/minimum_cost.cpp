#include <bits/stdc++.h> 
using namespace std; 

int minimum(int a, int b, int c){
    return min(a, min(b,c));
}

int minimum_cost_dp(int ** input, int n, int m){
    int ** output = new int*[n];
    for(int i =0; i < n; i++){
        output[i] = new int[m];
    }
    output[n-1][m-1] = input[n-1][m-1];
    for(int i = n-2; i >=0 ; i-- ){
        output[i][m-1] = output[i+1][m-1] + input[i][m-1];
    }
    for(int i = m - 2; i >= 0; i--){
        output[n-1][i] = output[n-1][i+1] + input[n-1][i];
    }
    for(int i = n-2; i >=0; i--){
        for(int j = m-2; j >=0; j--){
            output[i][j] =  input[i][j] + minimum(output[i+1][j], output[i+1][j+1], output[i][j+1]);
        }
    }
    int ans = output[0][0];
    delete [] output;
    return ans;
}

int minimum_cost_recursion(int ** input, int si, int sj, int ei, int ej){
    
    
    if(si == ei && sj == ej){
        return input[ei][ej];
    }
    if(si > ei || sj > ej){
        return INT_MAX;
    }
    int first = minimum_cost_recursion(input,si + 1, sj, ei, ej);
    int second = minimum_cost_recursion(input,si, sj + 1, ei, ej);
    int third = minimum_cost_recursion(input,si + 1, sj + 1, ei, ej);
    return input[si][sj] + minimum(first, second, third);
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
    int n, m;
    cin >> n >> m;
    int ** input = new int*[n];
    for(int i =0; i <= n; i++){
        input[i] = new int[m];
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> input[i][j];
        }
    }
    
    int si, sj, ei, ej;
    cin >> si >> sj >> ei >> ej;
    
    cout << minimum_cost_recursion(input,si, sj, ei, ej) << endl;
    cout << minimum_cost_dp(input, ei + 1, ej + 1) << endl;
} 