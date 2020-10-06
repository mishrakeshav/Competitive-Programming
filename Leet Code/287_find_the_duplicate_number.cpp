class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int fast = nums[0];
        int slow = nums[0];
        while(true){
            fast = nums[nums[fast]];
            slow = nums[slow];
            if(fast==slow) break;
        }
        slow = nums[0];
        while(slow!=fast){
            fast = nums[fast];
            slow = nums[slow];
        }
        return fast;
    }
};
