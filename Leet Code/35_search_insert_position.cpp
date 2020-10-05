class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left,right,mid;
        left = 0;
        right = nums.size();
        while(left < right){
            mid = left + (right-left)/2;
            if (target <= nums[mid]){
                right = mid;
            }else{
                left = mid + 1;
            }
        }
        return left;
    }
};
