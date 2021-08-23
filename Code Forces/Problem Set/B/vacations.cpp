#include<bits/stdc++.h>
#define INF 1000000000
#define endl '\n'
const double PI = 3.141592653589793238460;
const int mxN = 2e5;


using namespace std;


void solve(int n, vector<int> & vacations){
    vector<int> dp(n+1,0);
    for(int i = 0; i < n; i++){
        if(vacations[i] == 0){
            dp[i+1] = dp[i] + 1; 
        }
        else {
            if(i-1>=0 && vacations[i-1] == vacations[i] && vacations[i]!=3){
                dp[i+1] = dp[i] + 1;
            }else{
                dp[i+1] = dp[i];
            }
        }
    }
    for(int i = 0; i <= n; i++){
        cout << dp[i] << " ";
    }
    cout << endl;
    cout << dp[n] << endl;
}

int main(){
    ios_base::sync_with_stdio(0);
    int n,v;
    cin >> n;
    vector<int> vacations;
    for(int i = 0; i < n; i++){
        cin >> v;
        vacations.push_back(v);
    }
    solve(n,vacations);
}