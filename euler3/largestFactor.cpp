#include <iostream>
using namespace std;

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
