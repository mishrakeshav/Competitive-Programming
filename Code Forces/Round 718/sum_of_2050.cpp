#include<bits/stdc++.h>
// #include <sys/resource.h>
#define INF 1000000000
#define endl '\n'
const double PI = 3.141592653589793238460;
const int mxN = 2e5;


using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    long long n;
    while(t--){
        cin >> n;
        if(n%2050){
            cout << -1 << endl;
        }else{
            long long k = n/2050;
            long long ans = 0;
            while(k){
                ans += k%10;
                k /= 10;
            }
            cout << ans << endl;
        }   
    }

    
}