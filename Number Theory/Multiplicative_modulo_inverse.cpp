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
	myAns.y = (smallAns.x - ((a/b)*(smallAns.y)));

	return myAns;

}

Triplet modInverse(int A, int M){

    Triplet ans = gcdExtendedEuclid(A,M);
    return ans;
}


int main() {
	// your code goes here
	int a,b;
	cin >> a >> b;

	if(b > a){
		int temp = b;
		b = a;
		a = temp;
	}
	Triplet ans = modInverse(a,b);
	cout << ans.y << endl;


	return 0;
}
