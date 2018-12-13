#include <iostream>
using namespace std;

//Script that finds the largest prime factor of a number.
//It does this by starting the base at 2 and progressively dividing by the smallest valid divisor until we are left with a prime.
//This is necessarily the largest prime factor: in doing this we have represented our original number as a product of numbers
//at most as large as our result.

long long divide(long long number, long long base){
	if ((number%base == 0) and (number!=base)){
		return divide(number/base, base);
	}
	else if ((base*base > number) or (base == number)){
		return number;
	}
	else{
		base += 1;
return divide(number, base);
	}
}
int main(int argc, char** argv){
	long long toFactor = atoll(argv[1]);
	cout << divide(toFactor,2) << endl;
	return 0;
}
