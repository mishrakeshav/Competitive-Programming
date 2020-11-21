#include "solution.hpp"
using namespace std;

class Solution {
    public:
    string solve(string s0, string s1, int n) {
        return helper(s0,s1,n);
    }
    string helper(string& s1,string& s2, int i){
        if(i == 0) return s1;
        if(i == 1) return s2;
        if(i%2){
            return helper(s1,s2,i-2) + helper(s1,s2,i-1);
        }else{
            return helper(s1,s2,i-1) + helper(s1,s2,i-2);
        }
    }
};
