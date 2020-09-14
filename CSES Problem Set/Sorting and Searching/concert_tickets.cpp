#include<bits/stdc++.h>
#define mod 1000000007
#define pb push_back
#define ff first
#define ss second
#define ii pair<int,int>
#define vi vector<int>
#define vii vector<ii>
#define lli long long int
#define INF 1000000000
#define endl '\n'
const double PI = 3.141592653589793238460;
typedef std::complex<double> Complex;
typedef std::valarray<Complex> CArray;

using namespace std;




int main(){
    int n, m, k;
    cin >> n >> m;
    int h[n+1];
    vii t;
    for(int i = 0; i < n; i++){
        cin >> h[i];
    }
    for(int i = 0; i < m; i++){
        cin >> k;
        t.pb(make_pair(i,k));
    }
    sort(h, h + n, greater<>());
    sort(t.begin(),t.end(), greater<>());
    int i = 0, j =0;
    while(i < n && j < m){
        if()
    }
    // for(int i=0; i < n; i++){
    //     cout << h[i] << " ";
    // }
    // cout << endl;
    // for(int i = 0; i < m; i++){
    //     cout << t[i] << " ";
    // }
    cout << endl;
    return 0;
}