#include <bits/stdc++.h> 
using namespace std; 
void solve(); 
int kadane(int * arr, int n){
    int cur_sum = 0;
    int max_sum = 0;
    for(int i = 0; i < n; i++){
        cur_sum = cur_sum + arr[i];
        max_sum = max(cur_sum, max_sum);
        if(cur_sum < 0){
            cur_sum = 0;
        }
    }
    
    return max_sum;
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
{   
    int n;
    
    cin >> n;
    int arr[n];
    for(int i = 0; i < n; i++){
        cin >> arr[i];
        
    }
    
    cout << kadane(arr,n) ;
} 