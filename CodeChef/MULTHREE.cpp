#include<iostream>
using namespace std;

#define ll long long 

int main(){
    ios::sync_with_stdio(0);
	cin.tie(0);
    ll t;
    cin >> t;
    while(t--){
        ll K,d0,d1;
        cin >> K >> d0 >> d1 ;
        ll s = (d0 + d1);
        ll c = ((2*s)%10) + ((4*s)%10) + ((8*s)%10) + ((6*s)%10);
        ll cycles = (K-3)/4 ;
        ll total = 0 ;

        if (K==2){
            total = s;
        }
        else{
            total = 2*s + (c* 1LL * cycles);
            ll left_over = (K-3) - (cycles*4);
            ll p = 2;
            int i;

            for(i=1;i<=left_over;i++){
                total += (p*s)%10;
                p = (p*2)%10;
            }
        }
        cout << total << endl;
        if (total%3 !=0){
            cout << "NO\n";
        }
        else{
            cout << "YES\n";
        }
    }

    return 0;
}
