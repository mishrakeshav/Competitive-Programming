class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        unordered_map<int,int> hashmap;
        int n = nums.size();
        for(int i = 0; i < n; i++){
            if(hashmap.find(nums[i]) != hashmap.end()) {
                return nums[i];
            }
            hashmap[nums[i]] = 1;
        }
        return -1;
    }
};
