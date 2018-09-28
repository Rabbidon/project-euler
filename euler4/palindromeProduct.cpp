#include <iostream>
#include <array>
#include <cmath>
using namespace std;

int main(){
	array<int,900> palinArray;
	for (int a = 100; a < 1000; a = a+1){
		string str = to_string(a);
		string rev = str;
		swap (rev[0],rev[2]);
		palinArray[a-100] = stoi(str +rev);
	}
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
