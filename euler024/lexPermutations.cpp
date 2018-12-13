#include <iostream>
#include <vector>
using namespace std;

//Our goal is to find the (lexicographically) millionth permutation of the digits 0 through 9.
//This could be easily done with any standard permutations function, but I feel that defeats the point of the exercise.
//Instead we will do something weird, which is to take the number 999999 to "base factorial" (the 0th permutation here counts, hence the off-by-one).
//This is a term I just made up, but itis shorthand for the following algorithm:
int main(){

	//We store the digits from 0 to 9 in ascending order.
	vector<int> digits = {};
	for (int i = 0; i < 10; i++){
		digits.push_back(i);
	}

	int factorial = ((((((9*8)*7)*6)*5)*4)*3)*2;
	int remainder = 999999;
	//Ok, here goes: there are 9! perumations starting with each digit, so the first digit of our
	//representation of 999999 in "base factorial" will be the 1+(999999/(9!))th digit in our ordered list (integer division). This digit has been used, so we take
	// it out of the digit list, set our new number as 999999/(9!) and now we solve this subproblem in the same way. Repeat until we run out of digits.
	10000
	for (int j = 9; j >=1; j--){
		cout << digits[remainder/factorial] << endl;
		digits.erase(digits.begin() + remainder/factorial);
		remainder = remainder%factorial;
		factorial = factorial/j;
	}
	return 0;
}
