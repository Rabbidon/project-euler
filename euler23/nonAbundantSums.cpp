#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main(int argc, char** argv){
	int bound = atoi(argv[1]);
	int bigArray [bound] = {};
	vector<int> abundants = {};

	for (int i = 1; i <= bound; i++){
		int factorTotal = 0;
		for (int j = 2; j <= sqrt(i); j++){
			if (i%j == 0){
				factorTotal += j;
				if (j*j != i){
					factorTotal += (i/j);
				}
			}
		}
		if (factorTotal > i){
			abundants.push_back(i);
		}
	}

	int abundantNumber = abundants.size();

	for (int k = 0; k < abundantNumber; k++){
		for (int l = k; l < abundantNumber; l++){
			int candidate = abundants[l] + abundants[k];
			if (candidate <=  bound){
				bigArray [candidate - 1] = 1;
			}
		}
	}

	int nonAbundantSum = 0;
	for (int m = 0; m < bound; m++){
		nonAbundantSum += (1 - bigArray[m])*(m+1);
		if (1 - bigArray[m]){
		}
	}

	cout << nonAbundantSum << endl;
	return 0;
}
