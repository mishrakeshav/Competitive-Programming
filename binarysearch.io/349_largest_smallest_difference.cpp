int solve(vector<int>& nums, int k) {
    sort(nums.begin(),nums.end());
    if(k == 1) return 0;
    int n = nums.size();
    int diff = INT_MAX;
    for(int i = 0; i < n-k + 1; i++){
        int d = nums[i + k - 1] - nums[i];
        diff = min(d,diff);
    }
    return diff;
}