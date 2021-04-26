#include<bits/stdc++.h>
#include <sys/resource.h>
#define INF 1000000000
#define endl '\n'
const double PI = 3.141592653589793238460;
const int mxN = 2e5;


using namespace std;


int main(){
    rlimit cpu_time{.rlim_cur = 1, .rlim_max = 5}; 
    setrlimit(RLIMIT_CPU, &cpu_time);
    ios_base::sync_with_stdio(0);
    int tt;
    cin >> tt;
    while(tt--){
        int n,m,val;
        cin >> n >> m;
        vector<vector<int>> brr(n,vector<int>(m,-1));
        vector<tuple<int,int,int>> all;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                cin >> val;
                all.emplace_back(val, i, j);
            }
        }
        sort(all.begin(),all.end());
        for(int i = 0; i < m; i++){
            int idx = get<1>(all[i]);
            brr[idx][i] = get<0>(all[i]);
        }
        for(int i = m; i < n*m; i++){
            int idx = get<1>(all[i]);
            for(int j = 0; j < m; j++){
                if(brr[idx][j]==-1){
                    brr[idx][j] = get<0>(all[i]);
                    break;
                }
            }
        }
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                cout << brr[i][j] << " ";
            }
            cout << endl;
        }
    }
    return 0;
    
}