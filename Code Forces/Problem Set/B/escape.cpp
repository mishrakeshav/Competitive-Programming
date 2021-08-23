#include<bits/stdc++.h>
#define INF 1000000000
#define endl '\n'
const double PI = 3.141592653589793238460;
const int mxN = 2e5;


using namespace std;


int main(){
    ios_base::sync_with_stdio(0);
    float p,d,t,f,c,z;
    cin >> p >> d >> t >> f >> c;
    int r = 0;
    while(p < d){
        z=(p*t)/(d-p);
        if(z*d>=c) break;
        t+=2*z+f;
        r+=1;
    }
    cout << r << endl;
}