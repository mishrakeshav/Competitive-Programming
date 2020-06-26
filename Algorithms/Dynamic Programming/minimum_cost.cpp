#include <bits/stdc++.h> 
using namespace std; 
int input[100][100];
int minimum_cost(int si, int sj, int ei, int ej){
    if(si == ei && sj == ej){
        return input[ei][ej];
    }
    if(si > ei || sj > ej){
        return INT_MAX;
    }
    
    int first = minimum_cost(si + 1, sj, ei, ej);
    int second = minimum_cost(si, sj + 1, ei, ej);
    int third = minimum_cost(si + 1, sj + 1, ei, ej);
    return input[si][sj] + min(first, min(second, third));
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
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> input[i][j];
        }
    }
    
    int si, sj, ei, ej;
    cin >> si >> sj >> ei >> ej;
    for(int i = 0; i < ei; i++){
        for(int j = 0; j < ej; j++){
            input[i][j] = -1;
        }
    }
    cout << minimum_cost(si, sj, ei, ej);
} 