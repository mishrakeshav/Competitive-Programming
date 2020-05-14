#include<iostream>
#include<vector>
/*
Element access 
at(), front() , back() , data()

Modifiers 
insert(), emplace(), push_back()
emplace(), pop_back(), resize(), swap(), erase(), clear()
capacity(), size()

for setting the initial capacity of vector 
reserve() 
*/
using namespace std;

int main(){
    std::vector<int> arr1;
    int n,e;
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> e ;
        arr1.push_back(e);
    }
    for(int i = 0; i < n; i ++){
        cout << arr1[i] << endl;
    }
    //initialize a vector with size 5 and value of all elements equal to 20
    std::vector<int> arr2 (5,20);
    for(int i = 0; i < n; i ++){
        cout << arr2.at(i) << endl;
    }
    return 0;
}