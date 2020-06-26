#include <bits/stdc++.h> 
using namespace std; 
void solve(); 
/*
You have to find the number of ways to climb n steps
The number of steps you can take at a time is 1, 2, or 3 

*/
int stair_case(int n){
    if(n == 0){
        return 1;
    }
    if(n==1){
        return 1;
    }
    if(n==2){
        return 2;
    }
    int * output = new int[n+1];
    output[0] = 1;
    output[1] = 1;
    output[2] = 2;
    for(int i = 3; i <= n; i++){
        output[i] = output[i-1] + output[i-2] + output[i-3];
    }
    int result = output[n];
    delete [] output;
    return result;

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
{   int n;
    cin >> n;
    cout << stair_case(n);
} 