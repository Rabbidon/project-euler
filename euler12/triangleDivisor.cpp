#include <iostream>
#include <list>
#include <array>
using namespace std;

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
