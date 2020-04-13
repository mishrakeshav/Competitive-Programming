#include<iostream>
#include<set>
#include<vector>
using namespace std;
class Solution{
    public:
        int countElements(vector<int>& arr){
            set<int> s;
            for(int x:arr){
                s.insert(x)
            }
            int count = 0;
            for(int x:arr){
                if(s.count(x+1)==1){
                    count++;
                }
            }
            return count;
        }
}
