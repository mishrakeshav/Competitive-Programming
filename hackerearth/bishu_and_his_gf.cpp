#include<bits/stdc++.h>
using namespace std;
void dfs(int node, unordered_map<int,vector<int>> &graph, vector<int> &distance, int h){
    distance[node] = h + 1;
    for(int nbr: graph[node]){
        dfs(nbr,graph,distance,distance[node] + 1);
    }
}
int main(){
    int n;
    cin >> n;
    unordered_map<int,vector<int>> graph;
    vector<int> distance(n+1);
    for(int i = 1; i <=n; i++){
        graph[i] = {};
    }
    for(int i = 0; i < n-1; i++){
        int u,v;
        cin >> u >> v;
        graph[u].emplace_back(v);
    }
    dfs(1,graph,distance,0);
    int q,id;
    cin >> q;
    int dis = INT_MAX;int node = INT_MAX;
    for(int i = 0; i < q; i++){

        cin >> id;
        if(distance[id] < dis){
            dis = distance[id];
            node = id;
        }
        else if(distance[id] == dis && id < node){
            node = id;
        }
    }
    cout << node << endl;
    return 0;
}