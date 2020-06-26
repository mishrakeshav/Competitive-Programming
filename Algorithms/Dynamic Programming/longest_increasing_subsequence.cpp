#include <bits/stdc++.h> 
using namespace std; 
void solve(); 
/*
We start by taking the longest increasing subsequence 
till the ith element. 
We do this by maintaining an array Output where we store the 
longest increasing subsequence till the ith element
Then if we want the longest increasing subsequence till the ith element
we look back at all the previous element which is smaller than the 
current element and has the longest increasing subsequence .

Complexity : O(n^2)

*/


int lis(int * input, int n){
    int * output = new int[n];
    output[0] = 1;
    int best = 0;
    for(int i=1; i < n; i++){
        output[i] = 1;
        for(int j = i - 1; j >=0; j--){
            if(input[j] < input[i]){
                output[i] = max(output[j] + 1, output[i]);
            }
        }
        best = max(output[i],best);
    }
   
    return best;

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
    
    
        
        solve(); 
        cout << "\n"; 
    
   
  
    cerr << "time taken : " << (float)clock() / CLOCKS_PER_SEC << " secs" << endl; 
    return 0; 
} 
void solve() 
{ 
    int n;
    cin >> n;
    int * input = new int[n];
    for(int i = 0; i < n; i++){
        cin >> input[i];
    }
    cout << lis(input, n);
    delete [] input;
} 