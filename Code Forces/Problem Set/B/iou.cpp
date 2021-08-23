#include<bits/stdc++.h>
#define INF 1000000000
#define endl '\n'
const double PI = 3.141592653589793238460;
const int mxN = 2e5;


using namespace std;


int main(){
    ios_base::sync_with_stdio(0);
    int n,m;
    unordered_map<int,int> debts;
    cin >> n >> m;
    for(int i = 1; i <=m; i++){
        int a,b,c;
        cin >> a >> b >> c;
        debts[a] += c;
        debts[b] -= c;
    }
    int final_debt = 0;
    for(int i = 0; i <= n; i++){
        if(debts[i] > 0){
            final_debt += debts[i];
        }
    }
    cout << final_debt << endl;
}