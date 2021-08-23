#include<bits/stdc++.h>
#define INF 1000000000
#define endl '\n'
const double PI = 3.141592653589793238460;
const int mxN = 2e5;


using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    string s;
    getline(cin,s);
    int l = -1, ans = 0;
    for(int i = 0; s[i]; i++){
        l = (s.substr(i)).find("bear");
        ans += l!=-1?s.size()-i-3-l:0;        
    }
    cout << ans << endl;
}