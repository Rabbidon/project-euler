#include <iostream>
#include <cmath>
using namespace std;

//We are given a sum of 100 50-digit numbers and are asked to calculate the first 10 digits.
//This solution represents each number as digit arrays and adds each place in the number separately
//It first adds on the 10 entries of least value, and then works its way up, adding the next solution
//and dividing by 10 (place shifting) until it runs out of input. The first 10 digits can easily be read from the output.

int main(int argc, char** argv){
	string str(argv[1]);
	int sumArray [50] = {};
	for (int i = 0; i < 100; i++){
		for (int j = 0; j < 50; j++){
			sumArray [j] += str[j+i*50] - '0';
			cout << str[j+i*50] - '0' << endl;
		}
	}
	int digits = 10;
	long result = 0;
	for (int a = 0; a < digits; a++){
		result += sumArray[49 - a]*pow(10,a);
	}
	cout << result << endl;
	for (int b = digits; b < 50 ; b++){
		result += sumArray[49 - b]*pow(10,digits);
		result = result/10;
	}
	cout << result << endl;
}
