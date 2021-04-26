#include<bits/stdc++.h>
// #include <sys/resource.h>
#define INF 1000000000
#define endl '\n'
const double PI = 3.141592653589793238460;
const int mxN = 2e5;


using namespace std;

int dfs(vector<vector<int>> &board, int i, int j, int val, int k, int n){
    vector<int> di = {  -1, 0, 1};
    vector<int> dj = { 0, -1,  0};
    if(k == 0){
        return 0;
    }
    int prev = k;
    if(board[i][j] == -1){
        board[i][j] = val;
        for(int a = 0; a < 3 & k > 0; a++){
            int x = i + di[a];
            int y = j + dj[a];

            if( x < n && x >= 0 && y < n && y >= 0 && x!=y && board[x][y] == -1){
                k = dfs(board,x,y,val,k-1,n);
            } 
            if (k == 0) return 0;
        }
    }
    return k;
}


int main(){
    // rlimit cpu_time{.rlim_cur = 1, .rlim_max = 5}; 
    // setrlimit(RLIMIT_CPU, &cpu_time);
    ios_base::sync_with_stdio(0);
    int n;
    cin >> n;
    vector<vector<int>> board(n,vector<int>(n,-1));
    vector<int> p(n);
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(j > i){
                board[i][j] = 0;
            }
        }
    }
    for(int i = 0; i < n; i++){
        cin >> p[i];
    }
    for(int i = 0; i < n; i++){
        dfs(board,i,i,p[i],p[i],n);
             for(int a = 0; a < n; a++){
    }
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(board[i][j] !=0){
                cout << board[i][j] << " ";
            }
        }
        cout << endl;
    }

    return 0;
    
}