#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
long long inf = 1e9 + 1;
int main(){
    int t;
    cin >> t;
    while(t--){
        ll n;
        ll x[inf], y[inf];
        ll a, b;
        cin >> n;
        for(int i=0; i< inf; i++){
            x[i] = 0;
            y[i] = 0;
        }
        for(ll i = 0; i < 4*n-1; i++){
            cin >> a >> b;
            x[a] += 1;
            y[b] += 1;
        }
        for(ll i = 0; i < inf; i++){
            if (x[i]%2){
                a = x[i];
            }
            if(y[i]%2){
                b = y[i];
            }
        }
        cout << a << " " << b << endl;
    }
}