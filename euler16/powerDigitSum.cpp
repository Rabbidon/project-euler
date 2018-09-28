#include <iostream>
#include <list>
using namespace std;

int main(int argc, char** argv){
	int power = atoi(argv[1]);
	list<int> mult = {1};
	for (int i = 0; i < power; i++){
		list<int> tempMult = mult;
		int carry = 0;
		mult = {};
		for (list<int>::iterator it = tempMult.begin(); it != tempMult.end(); it++){
			mult.push_back ((2*(*it))%10 + carry);
			carry = ((2*(*it))/10);
		}
		if (carry){
			mult.push_back (1);
		}
	}
	int total = 0;
	for (list<int>::iterator it2 = mult.begin(); it2 != mult.end(); it2++){
		total += (*it2);
	}
	cout<< total << endl;
	return 0;
}
