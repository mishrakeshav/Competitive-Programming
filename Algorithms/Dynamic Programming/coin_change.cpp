#include <bits/stdc++.h> 
using namespace std; 
void solve(); 
int coin_change(int n, int * coins, int numd, int lookup_table){
    if(n==0){
        return 1;
    }
    if(n < 0){
        return 0;
    }
    if(numd == 0){
        return 0;
    }
    if(lookup_table[n][numd] > 0){
        return lookup_table[n];
    }

    int first = coin_change(n - coins[0], coins, numd, lookup_table);
    int second = coin_change(n, coins + 1,numd-1, lookup_table);
    lookup_table[n][numd] = first + second;
    return lookup_table[n][numd]

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
{   int n, numd;
    cin >> n;
    cin >> numd;
    int * coins = new int [numd];
    for(int i = 0; i < n; i++){
        cin >> coins[i];
    }
    int * input = new int[n];
    for(int i = 0; i < n; i++){
        cin >> input[i];
    }
    int lookup_table[n+1][numd + 1];
    for(int i = 0; i<= n; i++ ){
        for(int j = 0; j <= numd; j++){
            lookup_table[i][j] = -1;
        }
    }

    cout << coin_change(n, coins, numd, lookup_table) ;

} 