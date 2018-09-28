#include <iostream>
using namespace std;

int main(int argc, char** argv){
	string str = string(argv[1]);
	int lnth = str.length();
	int consec = atoi(argv[2]);
	if (lnth < consec){
		cout << "you fucked up" << endl;
		return 0;
	}
	long maxProd = 0;
	for (int i = 0; i<=(lnth-consec); i ++){
		long prod = 1;
		for (int a = 0; a<consec; a++){
			prod = prod * ((str.at(a+i))-'0');
		}
		if (prod > maxProd){
			maxProd = prod;
		}
	}
	cout << maxProd << endl;
	return 0;
}
