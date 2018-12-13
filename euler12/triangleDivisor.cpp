#include <iostream>
#include <list>
#include <array>
using namespace std;

//Code to determine the first triangle number with over k distinct factors, for some given k.
//The number of factors of PRODUCT over i of ((a_i)^(b_i)) is PRODUCT over i of (1+(b_i)).
//This solution just uses this approach with brute force, but we can speed up our factorisation by noting that
//the nth triangle number is n(n-1)/2, so we can just factorise n and n-1 instead, and combine their factors.
//This means that, if the nth triangle number is the one we need, we only have to factorise the first n numbers.
//The required test case was not sufficiently large to warrant the extra footling required to implement this though.
int main(int argc, char** argv){
	list<int> primes;
	int counter = 0;
	for (int i = 2; true; i++){
		bool primeFlag = true;
		int triangle = (i*(i-1))/2;
		int factorArray [counter+1] = {};
		int subCount = 0;
		for (list<int>::iterator it = primes.begin(); it != primes.end(); it++){
			if (i%*it == 0){
				primeFlag = false;
			}
			while (triangle%(*it) == 0){
				triangle = triangle/(*it);
				factorArray[subCount]++;
			}
			subCount++;
		}
		if (primeFlag){
			counter = counter + 1;
			primes.push_back(i);
			factorArray[counter] = 1;
		}
		int prod = 1;
		for (int c = 0; c < counter; c++){
			prod = prod*(factorArray[c]+1);
		}
		if (prod>atoi(argv[1])){
			cout << (i*(i-1))/2 << endl;
			return 0;
		}
	}
}
