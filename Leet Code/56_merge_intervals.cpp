class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        int n = intervals.size();
        if(n == 1 || n == 0) return intervals;
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> ans;
        ans.push_back(intervals[0]);
        int j = 0;
        for(int i = 0; i < n; i++){
            if(ans[j][1] >= intervals[i][0]){
                if(ans[j][0] > intervals[i][0]){
                    ans[j][0] = intervals[i][0];
                }
                if(ans[j][1] < intervals[i][1]){
                    ans[j][1] = intervals[i][1];
                }
            }else{
                ans.push_back(intervals[i]);
                j++;
            }
        }
        return ans;
    }
};