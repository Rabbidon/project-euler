#include <iostream>
#include <cmath>
using namespace std;

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
