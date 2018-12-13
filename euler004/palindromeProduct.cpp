#include <iostream>
#include <array>
#include <cmath>
using namespace std;

//Funtion to find the greatest palindromic number that is the product of 2 3-digit numbers.
//We start with all possible palindromes and test divisibility in reverse size order until we find a solution.
int main(){
	//Any candidate palindrome is necessarily 5 or 6 digits(between 100^2 and 1000^2). This algorithm is optimistic and assumes the
	//existence of a 6-digit palidrome of the required form. Therefore this will create all candidate palindromes
	array<int,900> palinArray;
	for (int a = 100; a < 1000; a = a+1){
		string str = to_string(a);
		string rev = str;
		swap (rev[0],rev[2]);
		palinArray[a-100] = stoi(str +rev);
	}
	//This loop checks each candidate for the larger 3-digit factor by divisibility testing.
	for (int i = 899; i >= 0; i = i-1){
		int squareRoot = static_cast<int>(ceil(sqrt(float(palinArray[i]))));
		for (int b = squareRoot; b < min(1000,(palinArray[i]/100)); b = b+1){
			if (palinArray[i]%b == 0)
			{
				cout << b << endl;
				cout << palinArray[i] << endl;
				return 0;
			}
		}
	}

}
