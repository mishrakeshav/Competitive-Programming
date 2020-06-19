#include<iostream>
#include<array>
using namespace std;
//g++ arrays.cpp -o arrays.exe

int main(){
    //size of array should be given at complie time
    std::array<int,5> arr = {1,2,3,4,5};
	
    cout << arr.data() << endl;
    cout << arr.at(1) << endl;
    cout << arr.front() << endl;
    cout << arr.back() << endl;
    cout << arr[1] << endl;
    
    return 0;
}