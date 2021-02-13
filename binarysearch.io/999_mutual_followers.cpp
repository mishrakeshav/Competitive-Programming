vector<int> solve(vector<vector<int>>& relations) {
    unordered_map<int,unordered_set<int>> s;
    for(int i = 0; i < relations.size(); i++){
        int a = relations[i][0];
        int b = relations[i][1];
        s[a].insert(b);
    }
    vector<int> ans;
    unordered_set<int> completed;
    for(int i = 0; i < relations.size(); i++){
        int a = relations[i][0];
        int b = relations[i][1];
        if(!(s[a].find(b)==s[a].end()) && !(s[b].find(a)==s[b].end())){
            if((completed.find(a)==completed.end())){
                ans.push_back(a);
                completed.insert(a);
            }
        }
    }
    sort(ans.begin(),ans.end());
    return ans;
}