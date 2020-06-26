#include <bits/stdc++.h> 
using namespace std; 
void solve();
int num_codes(int * input, int size){

    if(size == 0){
        return 1;
    }
    if(size ==1){
        return 1;
    }
    int * output = new int[size + 1];
    output[0] = 1;
    output[1] = 1;
    for(int i=2; i<= size; i++){
        output[i] = 0;
    }
    for(int i=2; i<= size; i++){
        output[i] += output[i-1];
        if(input[i-2]*10 + input[i-1] <= 26){
            output[i] += output[i-2];
        }
    }
    for(int i=0; i<= size; i++){
        cout << output[i] << " ";
    }
    cout << "\n";
    int ans = output[size];
    delete [] output;
    return ans;
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
{   int size;   
    cin >> size;
    int * arr = new int[size];
    for(int i=0; i< size; i++){
        cin >> arr[i];
    }
    cout << num_codes(arr,size);
    
} 