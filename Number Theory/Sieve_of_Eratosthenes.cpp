#include <iostream>
using namespace std;

int makeSieve(int n){
	bool isPrime[n+1];
	for(int i = 0; i<=n;i++){
		isPrime[i] = true;
	}
	
	isPrime[0] = false;
	isPrime[1] = false;
	
	for(int i = 2;i*i<=n; i++){
		if(isPrime[i]){
			for(int j = i*i ; j <= n ; j += i){
				isPrime[j] = false;
			}
		}
	}
	int count = 0;
	for(int i=0; i<=n; i++){
		if (isPrime[i]){
			count++;
		}
	}
	return count;
	
}

int main() {
	int n;
	cin >>n;
	
	int number_of_primes = makeSieve(n);
	cout << number_of_primes << endl;
	return 0;
}