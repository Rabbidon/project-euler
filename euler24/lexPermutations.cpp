#include <iostream>
#include <vector>
using namespace std;

int main(){

	vector<int> digits = {};
	for (int i = 0; i < 10; i++){
		digits.push_back(i);
	}

	int factorial = ((((((9*8)*7)*6)*5)*4)*3)*2;
	int remainder = 999999;
	for (int j = 9; j >=1; j--){
		cout << digits[remainder/factorial] << endl;
		digits.erase(digits.begin() + remainder/factorial);
		remainder = remainder%factorial;
		factorial = factorial/j;
	}
	return 0;
}
