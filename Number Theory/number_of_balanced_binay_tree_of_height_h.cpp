#include <iostream>
#include <cmath>
using namespace std;

long balancedBts(int h){
	if(h==1 || h==0){
		return 1;
	}
	long m = pow(10,9) + 7;
	
	long x = balancedBts(h-1)%m;
	long y = balancedBts(h-2)%m;
	
	return (x*x)%m + (2*x*y)%m;
	
	
}

int main() {
	// your code goes here
	int h;
	cin >> h;
	cout << balancedBts(h) << endl;
	return 0;
}