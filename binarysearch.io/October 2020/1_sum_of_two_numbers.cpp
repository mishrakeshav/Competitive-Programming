#include "solution.hpp"
using namespace std;

class Solution{
    public:
    bool solve(vector<int>& nums, int k){
        unordered_map<int,int> hashmap;
        if(hashmap.find(k-nums[i]) != hashmap.end()){
            return true;
        }
        hashmap[nums[i]] = 1;
    }
    return false;
}
