class Solution {
public:
    void sortColors(vector<int>& nums) {
        int low = 0;
        int mid = 0;
        int swap;
        int high = nums.size() - 1;
        while(mid <= high){
            if(nums[mid] == 0){
                swap = nums[mid];
                nums[mid] = nums[low];
                nums[low] = swap;
                mid++;
                low++;
            }else if(nums[mid] == 2){
                swap = nums[mid];
                nums[mid] = nums[high];
                nums[high] = swap;
                high--; 
            }else if(nums[mid] == 1){
                mid++;
            }
        }
    }
};
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int red = 0;
        int white = 0;
        int blue = 0;
        for(int x:nums){
            if(x==0) red++;
            else if(x==1) white++;
            else if(x==2) blue++;
        }
        for(int& x: nums){
            if(red){
                x = 0;
                red--;
            }
            else if(white){
                x = 1;
                white--;
            }else{
                x = 2;
                blue--;
            }
        }
    }
};
