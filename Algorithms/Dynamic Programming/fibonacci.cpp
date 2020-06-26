#include <bits/stdc++.h> 
using namespace std; 
int fibo(int n,int * arr){
    if(arr[n]){
        return arr[n];
    }
    
    for(int i =2; i <=n; i++){
        arr[i] = arr[i-1] + arr[i-2];
    }
    return arr[n];
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
    int n;
    cin >> t; 
    while (t--) { 
        cin >> n;
        int * arr = new int[n + 1]; 
        arr[0] = 1;
        arr[1] = 1;
        for(int i = 2; i <= n; i++){
            arr[i] = 0;
        }
        cout << fibo(n, arr) ;
        cout << "\n"; 
    
    } 
  
    cerr << "time taken : " << (float)clock() / CLOCKS_PER_SEC << " secs" << endl; 
    return 0; 
} 
