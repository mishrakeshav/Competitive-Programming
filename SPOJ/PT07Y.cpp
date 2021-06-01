#include<bits/stdc++.h>
using namespace std;

void dfs(int node, unordered_map<int, vector<int>> &graph, vector<int> &visited){
    if(visited[node]==1) return;
    visited[node] = 1;
    for(int nbr :  graph[node]){
        dfs(nbr,graph,visited);
    }
}

int main(){
    int n,m;
    cin >> n >> m;
    unordered_map<int,vector<int>> graph;
    vector<int> visited(n+1,0);
    for(int i = 1; i <= n; i++){
        graph[i] = {};
    }
    for(int i = 1; i <= m; i++){
        int u,v;
        cin >> u >> v;
        graph[u].emplace_back(v);
        graph[v].emplace_back(u);
    }
    if(m != n-1){
        cout << "NO" << endl;
    }else{
        dfs(1,graph,visited);
        int isTree = 1;
        for(int i = 1; i <= n; i++){
            if(visited[i]==0){
                isTree = 0;
                break;
            }
        }
        if(isTree==1){
            cout << "YES" << endl;
        }else{
            cout << "NO" <<  endl;
        }
    }
}