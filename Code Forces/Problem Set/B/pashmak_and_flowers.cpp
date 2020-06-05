#include<iostream>
#include<climits>
using namespace std;
const int INF = 1000000000;
const int MAX = 200005;
int a[MAX];
int main(){
    ios::sync_with_stdio(false);
    long long n;
    cin >> n;
    int mn = INF,mx = 0;

    for(int i=0;i<n;i++){
        cin >> a[i];
        mn = min(mn,a[i]);
        mx = max(mx,a[i]);
    }

    long long t1 = 0, t2 = 0;
    for(int i=0; i < n; i++){
        t1 += (a[i]==mn);
        t2 += (a[i]==mx);
    }
    cout << mx-mn << " ";
    if(mn==mx){
        cout << n*(n-1)/2;
    }
    else{
        cout << mn*mx ;
    }

    return 0;
}
