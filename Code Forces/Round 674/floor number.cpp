#include<bits/stdc++.h>
#define ll long long int
using namespace std;
int main()
{
    ll t;
    cin >> t;
    while(t--)
    {
        long double n,x;
        cin >> n >> x;
        if(n==1 || n==2){
            cout << 1 << endl;
        }
        else{
            cout << ceil((n - 2) / x) + 1 << endl;
        }
    }
    return 0;
}