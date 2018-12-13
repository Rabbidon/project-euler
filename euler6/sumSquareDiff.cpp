#include <iostream>
using namespace std;

//This is just a brute-force calculation of square of sum minus sum of squares.
int main(int argc, char** argv){
	long number = atol(argv[1]);
	long squareSum = 0;
	long sum = 0;
	for (long a = 1; a <= number;  a++){
		sum = sum + a;
		squareSum = squareSum + a*a;
	}
	long sumSquared = sum*sum;
	cout << sumSquared - squareSum<< endl;
	return 0;
}
