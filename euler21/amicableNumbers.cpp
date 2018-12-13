#include <iostream>
#include <cmath>
using namespace std;

//Calculates the sum of all amicable numbers under a certain bound.
//Amicable numbers are pairs of distict numbers that are equal to the sum of each other's divisors.
//Since we are iterating over a fixed range, we use the Sieve of Eratosthenes to sum all divisors.
//After this step, the 'partner' array shows the sum of divisors for each number in the required range.
int main(int argc, char** argv){
	int bound = atoi(argv[1]);
	int partner [bound] = {};
	int sum = 0;
	for (int i = 1; i <= bound; i++)
	{
		for (int j = 2*i; j<=bound; j+=i)
		{
			partner[j-1] += i;
		}
	}
	//We now check each number to see what amicable pairs exist.
	for (int k = 1; k <= bound; k++){
		int buddy = partner[k-1];
		if ((buddy <= bound)and(buddy != k)){
			if (partner[partner[k-1]-1] == k){
				sum += k;
			}
		}
	}
	cout << sum << endl;
	return 0;
}
