class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int m = nums.size();
        int s = 0;
        for(int i = 0; i < m; i++){
            s ^=(i+1)^(nums[i]);
        }
        return s;
    }
};
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int m = nums.size();
        int s = m*(m+1)/2;
        for(int x:nums){
            s -= x;
        }
        return s;
    }
};
