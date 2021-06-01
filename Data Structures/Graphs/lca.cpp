#include<bits/stdc++.h>
// #include <sys/resource.h>
#define INF 1000000000
#define endl '\n'
const double PI = 3.141592653589793238460;
const int mxN = 2e5;

using namespace std;

void dfs(int node, int h, 
    unordered_map<int,vector<int>> &tree, 
    vector<int> &height, vector<int> &euler, 
    vector<int> &first, vector<int> &visited
    ){
    if(visited[node]==1) return;
    visited[node] = 1;
    height[node] = h;
    first[node] = euler.size();
    euler.push_back(node);
    for(int nbr : tree[node]){
        if(visited[nbr]==0){
            dfs(nbr,h+1,tree,height,euler,first,visited);
            euler.push_back(node);
        }
    }
}
void printVector(vector<int> &arr){
    for(int i:arr){
        cout << i << " ";
    }
    cout << endl;
}
void query(int u, int v, vector<int> &euler, vector<int> &first, vector<int> &height){
    int minHeight = INF , node;
    int start = first[u], end = first[v];
    if(start > end){
        swap(start,end);
    }
    for(int i = start ; i <= end; i++){
        if(height[euler[i]] < minHeight){
            minHeight = height[euler[i]];
            node = euler[i]; 
        }
    }
    cout << node+1 << endl;
}

void solve(){
    int n,root,queries;
    cin >> n >> root >> queries;
    root--;
    unordered_map<int,vector<int>> tree;
    for(int i = 0; i < n-1; i++){
        int a,b;
        cin >> a >> b;
        tree[a-1].push_back(b-1);
    }
    vector<int> height(n),euler,first(n),visited(n,0);
    dfs(root,0,tree,height,euler,first,visited);
    
    printVector(euler);
    for(int i = 0; i < queries; i++){
        int u,v;
        cin >> u >> v;
        // query can be done using segment tree or square root decomposition
        query(u-1,v-1,euler,first,height);
    }

}

int main(){
    ios_base::sync_with_stdio(0);
    solve();
    
}