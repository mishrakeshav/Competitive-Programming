#include "solution.hpp"
using namespace std;

class Solution{
    public:
        int solve(vector<int>& nums){
            int max_1 = 32767;
            int max_2 = max_1;
            for(auto num:nums){
                if(num > max_1){
                    max_2 = max_1;
                    max_1 = num;
                }
                else if(num > max_2){
                    max_2 = num;
                }
            }  
            int m = max_1*max_2; 
            max_1 = -32767;
            max_2 = max_1;
            for(auto num:nums){
                if(num < max_1){
                    max_2 = max_1;
                    max_1 = num;
                }
                else if(num < max_2){
                    max_2 = num;
                }
            }   
            m = max(m,max_1*max_2);
            return m;  
        }
}
