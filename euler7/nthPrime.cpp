#include <iostream>
#include <cmath>
using namespace std;

int main(int argc, char** argv){
	int number = atoi(argv[1]);
	int primes [number];
	int counter = 0;
	for (int i = 2; counter<number ; i ++){
		bool primeFlag = 1;
		for (int b = 0; primes[b]<=sqrt(i) and b<counter; b++){
			if (i%primes[b] == 0){
				primeFlag = 0;
				break;
			}
		}
		if (primeFlag){
			primes[counter] = i;
			counter ++;
		}
	}
	cout << primes[number-1] << endl;
	return 0;
}
