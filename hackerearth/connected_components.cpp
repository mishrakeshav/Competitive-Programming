#include<bits/stdc++.h>
using namespace std;

void dfs(int node, unordered_map<int,vector<int>> &graph,vector<int> &visited){
    if(visited[node]==1) return;
    visited[node] = 1;
    for(int i: graph[node]){
        dfs(i,graph,visited);
    }
}

int main(){
    int n,e;
    cin >> n >> e;
    vector<int> visited(n+1,0);
    unordered_map<int,vector<int>> graph;
    for(int i = 1; i <= n; i++){
        graph[i] = {};
    }
    for(int i = 0; i < e; i++){
        int u,v;
        cin >> u >> v;
        graph[u].emplace_back(v);
        graph[v].emplace_back(u);
    }
    int components = 0;
    for(int i = 1; i <=n; i++){
        if(visited[i]==0){
            components++;
            dfs(i,graph,visited);
        }
    }
    cout << components << endl;
}