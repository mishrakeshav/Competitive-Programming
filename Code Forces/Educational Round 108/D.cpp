#include <iostream>
#include <bits/stdc++.h>
#define ll long long
using namespace std;
 
const int M = 1e9+7;
ll mod(ll x){
    return (x%M + M)%M;
}
 
ll mul(ll a, ll b){
    return mod((mod(a)*mod(b)));
}
 
void solve(){
    int n;
    cin>>n;
    vector<ll>a(n),b(n);
    for(int i=0;i<n;i++) cin>>a[i];
    for(int i=0;i<n;i++) cin>>b[i];
    ll ans=0;
    ll maxi;
    for(int i=0;i<n;i++) ans+=a[i]*b[i];
    maxi=ans;
    for(int i=0;i<n;i++){
        ll total=ans;
        int l=i-1;
        int r=i+1;
        while(l>=0 && r<n){
            total-=(a[l]*b[l] + a[r]*b[r]);
            total+=(a[l]*b[r] + a[r]*b[l]);
            maxi=max(maxi,total);
            l--;
            r++;
        }
    }
    for(int i=0;i<n;i++){
        ll total=ans;
        int l=i;
        int r=i+1;
        while(l>=0 && r<n){
            total-=(a[l]*b[l] + a[r]*b[r]);
            total+=(a[l]*b[r] + a[r]*b[l]);
            maxi=max(maxi,total);
            l--;
            r++;
        }
    }
    cout<<maxi;
}  
int main(){
    ios::sync_with_stdio(0);
            cin.tie(0);
            cout.tie(0);
            cout<<fixed;
            cout<<setprecision(10);
    //        freopen("timber_input.txt", "r", stdin);
    //        freopen("timber_output.txt", "w", stdout);
            int t=1;
            // cin>>t;
            for(int i=1;i<=t;i++){
            //    cout<<"Case #"<<i<<": ";  
                solve();
    }
    return 0;
}
 