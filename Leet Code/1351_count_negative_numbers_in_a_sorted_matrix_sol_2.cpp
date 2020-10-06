class Solution {
public:
    int binary_search(vector<int>& arr){
        int n = arr.size();
        int left = 0;
        int right = n - 1;
        int mid;
        while(left < right){
            mid = left + (right-left)/2;
            if(arr[mid] < 0){
                right = mid;
            }else{
                left = mid + 1;
            }
        }
        if(arr[right] >= 0) right++;
        return right;
    }
    int countNegatives(vector<vector<int>>& grid) {
        int n1 = grid.size();
        int n2 = grid[0].size();
        int count = 0;
        for(int i = 0; i < n1; i++){
            int a = binary_search(grid[i]);
            count += n2 - a;
        }
        return count;
    }
};
