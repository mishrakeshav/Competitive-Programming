#include <iostream>
#include <bits/stdc++.h>
#include<cmath>
using namespace std;
class Triplet{
public:
	int gcd;
	int x;
	int y;

};
Triplet gcdExtendedEuclid(int a, int b){
	if(b==0){
		Triplet myAns;
		myAns.gcd = a;
		myAns.x = 1;
		myAns.y = 0;

		return myAns;
	}

	Triplet smallAns = gcdExtendedEuclid(b,a%b);
	Triplet myAns;
	myAns.gcd = smallAns.gcd;
	myAns.x = smallAns.y;
	myAns.y = (smallAns.x - ((a/b)*smallAns.y));

	return myAns;

}

int gcd(int a,int b){

	if(a%b==0){
		return b;
	}
	return gcd(b,a%b);
}
int gcd_iterative(int a,int b){
	if(a%b == 0){
		return b;
	}
	while(a%b != 0){
		int temp = a%b;
		a = b;
		b = temp;
	}
	return b;
}
int main() {
	// your code goes here
	int a,b;
	cin >> a >>b;
	if(b > a){
		int temp = b;
		b = a;
		a = temp;
	}
	cout << gcd(a,b) << endl;
	cout << gcd_iterative(a,b) << endl;

	Triplet ans = gcdExtendedEuclid(a,b);
	cout << ans.gcd << endl;
	cout << ans.x << endl;
	cout << ans.y << endl;

	return 0;
}
