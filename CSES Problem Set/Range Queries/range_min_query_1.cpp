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
int st[800001] , arr[200001];
void build(int pos, int low, int high){
    if(low == high) {
        st[pos] = arr[low];
        return;
    }
    int mid = (low+high)/2;
    build(2*pos+1,low,mid);
    build(2*pos+2,mid+1,high);
    st[pos] = min(st[2*pos+1],st[2*pos+2]);
}
int query(int low, int high, int qlow, int qhigh, int pos){
    if(qlow > qhigh){
        return INF;
    }
    if(qlow == low && qhigh == high){
        return st[pos];
    }
    int mid = (low+high)/2;
    int left = query(low,mid,qlow,min(qhigh,mid),2*pos+1);
    int right = query(mid+1,high, max(qlow,mid+1), qhigh,2*pos+2);
    return min(left,right);
}
int main(){
    int n,q,l,r;
    cin >> n >> q;
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    
    build(0,0,n-1);
    cout << endl;
    for(int i = 0; i < q; i++){
        cin >> l >> r;
        cout << query(0,n-1,l-1,r-1,0) << endl;
    }
    return 0;
}