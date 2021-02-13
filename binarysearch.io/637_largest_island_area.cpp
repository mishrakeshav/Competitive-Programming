int dfs(int i,int j,int n, int m, vector<vector<int>>& matrix){
    if(!matrix[i][j]) return 0;
    matrix[i][j] = 0;
    vector<int> dx = {1,0,-1,0};
    vector<int> dy = {0,1,0,-1};
    int ans = 1;
    for(int a = 0; a < 4; a++){
        int x = j + dx[a];
        int y = i + dy[a];
        if(0 <= x && x < m && 0 <= y && y < n && matrix[y][x]){
            ans += dfs(y,x,n,m,matrix);
        }
    }
    return ans;
}


int solve(vector<vector<int>>& matrix) {
    int n,m;
    n = matrix.size();
    m = matrix[0].size();
    int ans =0;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            ans = max(dfs(i,j,n,m,matrix),ans);
        }
    }
    return ans;
}