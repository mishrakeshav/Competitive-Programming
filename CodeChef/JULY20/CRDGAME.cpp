#include <iostream>
using namespace std;
typedef long long ll;
int main(){
    ll t;
    cin >> t;
    while(t--){
        ll n;
        ll point_a = 0;
        ll point_b = 0;
        ll pow_a = 0;
        ll pow_b = 0;
        ll a;
        ll b;
        for(ll i=0; i<n; i++){
            
            cin >> a >> b;
            pow_a = 0;
            pow_b = 0;
            while(a){
                pow_a += a%10;
                a /= 10;
            }
            while(b){
                pow_b += b%10;
                b /= 10;
            }
            if(pow_a > pow_b){
                point_a += 1;
            }
            else if(pow_a < pow_b){
                point_b += 1;
            }
            else{
                point_a += 1;
                point_b += 1;
            }
        }
        if(point_a > point_b){
            cout << 0 << " " << point_a << endl;;
        }
        else if (point_a < point_b){
            cout << 1 << " " << point_b << endl;
        }
        else{
            cout << 2 << " " << point_a << endl;
        }
    }
    return 0;
}