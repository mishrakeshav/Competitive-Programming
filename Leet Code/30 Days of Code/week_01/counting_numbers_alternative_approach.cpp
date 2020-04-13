#include<iostream>
#include<vector>
#include<set>
#include <algorithm>
using namespace std;
//Better approach
int countElements(vector<int> arr){
    sort(arr.begin(),arr.end());
    int answer = 0 ;
    int prv = -1,prv_count = 0;

    for(int x:arr){
        if(x==prv){
            prv_count++;
        }
        else{
            if(x==prv+1){
                answer += prv_count;
            }
            prv = x;
            prv_count = 1;
        }
    }
    return answer;
}
