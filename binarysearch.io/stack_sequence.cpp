/*
Problem Link: https://binarysearch.io/problems/Stack-Sequence
Solution by Keshav Mishra
*/
#include "solution.hpp"
using namespace std;


class Solution {
    public:
    bool solve(vector<int>& pushes, vector<int>& pops) {
        int n1 = pushes.size();
        int n2 = pops.size();
        int i ,j;
        i = j = 0;
        vector<int> stack;
        while (i < n1 and j < n2){
            stack.push_back(pushes[i]);
            while(!stack.empty() && j < n2 && stack.back() == pops[j]){
                stack.pop_back();
                j++;
            } 
            i++;
        }
        while(!stack.empty() && j < n2 && stack.back() == pops[j]){
            stack.pop_back();
            j++;
        }
        return j == n2;
    }
};
