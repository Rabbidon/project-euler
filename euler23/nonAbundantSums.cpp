#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

//Finds all numbers under a certain bound that cannot be written as the sum of two abundant (factor sum exceeds number itself) numbers.

int main(int argc, char** argv){
	int bound = atoi(argv[1]);
	int bigArray [bound] = {};
	int factorSum [bound] = {};
	vector<int> abundants = {};

	//We find all abundant numbers (Sieve of Eratosthenes);

	for (int i = 1; i <= bound; i++){
		for (int j = 2*i; j <= bound; j+=i)
		{
			factorSum [j-i] += i;
		}
	}

	for (int i=1 ;i <= bound; i++)
	{
		if (factorSum[i-1]>i)
		{
			abundants.push_back(i);
		}
	}

	int abundantNumber = abundants.size();

	//We calculate all numbers under the bound that are the sum of two abundant numbers
	for (int k = 0; k < abundantNumber; k++){
		for (int l = k; l < abundantNumber; l++){
			int candidate = abundants[l] + abundants[k];
			if (candidate <=  bound){
				bigArray [candidate - 1] = 1;
			}
		}
	}

	//We sum all the numbers we found
	int nonAbundantSum = 0;
	for (int m = 0; m < bound; m++){
		nonAbundantSum += (1 - bigArray[m])*(m+1);
		if (1 - bigArray[m]){
		}
	}

	cout << nonAbundantSum << endl;
	return 0;
}
