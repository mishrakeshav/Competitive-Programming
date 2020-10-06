class Solution {
public:
    int busyStudent(vector<int>& startTime, vector<int>& endTime, int queryTime) {
        int arr[1002];
        for(int i = 0; i < 1002; i++){
            arr[i] = 0;
        }
        for(int i = 0; i < startTime.size(); i++){
            arr[startTime[i]] += 1;
        }
        for(int i = 0; i < endTime.size(); i++){
            arr[endTime[i] + 1] -= 1;
        }
        for(int i = 1; i < 1002; i++){
            arr[i] += arr[i-1];
        }
        return arr[queryTime];
    }
};
