// Problem LinK: https://binarysearch.io/problems/Minimum-Bracket-Addition
// Solution by Keshav Mishra
// #include "solution.hpp" 
using namespace std;


class Solution {
    public:
    int solve(string s) {
        // Write your code here
        int ch ,ans;
        ch = ans = 0;
        for(auto c:s){
            if (c == '(')
                ch++;
            else{
                if(ch){
                    ch--; 
                }else{
                    ans++;
                }
            }
        }
        ans += ch;
        return ans;
    }
};
