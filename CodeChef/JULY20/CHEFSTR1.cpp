#include <iostream>
using namespace std;
typedef long long ll;
int main(){
    ll t;
    cin >> t;
    while(t--){
        ll n;
        cin >> n;
        ll arr[n];
        for(ll i=0; i<n; i++){
            cin >> arr[i];
        }
        ll count = 0;
        for(ll i=1; i<n; i++){
            count += abs(arr[i-1]-arr[i]) - 1;
        }
        cout << count << endl;
    }
    return 0;
}