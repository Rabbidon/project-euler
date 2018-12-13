#include <iostream>
using namespace std;

//Iterates over a digit array to find the largest product of n consective numbers, for some fixed n. Here n is denoted by "consec".
int main(int argc, char** argv){
	string str = string(argv[1]);
	int lnth = str.length();
	int consec = atoi(argv[2]);
	if (lnth < consec){
		cout << "Invalid entry - product length exceeds number of digits" << endl;
		return 0;
	}
	//Calculates the product of the first n consecutive digits.
	long maxProd = 0;
	long prod = 1;
	for (int i = 0; i<=consec; i ++)
	{
		prod *= ((str.at(i))-'0');
	}
	//Efficiently calclates the product of each digit string of length n using the previous one: quotients by the first element of the string
	// and then multiplies by the first element after the string.
	for (int i = consec; i<=lnth; i ++){
		prod *= ((str.at(i))-'0');
		prod /= ((str.at(i-consec))-'0');
		if (prod > maxProd){
			maxProd = prod;
	}
	cout << maxProd << endl;
	return 0;
}
