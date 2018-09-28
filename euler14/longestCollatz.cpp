#include <iostream>
#include <list>
#include <vector>
#include <assert.h>
using namespace std;

int main(int argc, char** argv){
	int bound = atoi(argv[1]);
	vector<int> bigArray;
	bigArray.push_back(1);
	for (int i = 1; i < bound; i++){
		bigArray.push_back(0);
	}
        int maxChain = 1;
	int chainStart = 1;
	for (int j = 1; j < bound; j++){
		long long position = j;
		list<long long> elementList = {};
		while (true){
			elementList.push_back(position);
			if ((position+1)%2 == 0){
				position = (position+1)/2 - 1;
			}
			else{
				position = 3*(position+1);
			}
			if (position < bound){
				if (bigArray.at(position) != 0){
					break;
				}
			}
		}
		int counter = elementList.size();
		int tempCounter = counter;
		int reference = bigArray.at(position);
		for (list <long long>::iterator it = elementList.begin(); it != elementList.end(); it++){
			if (*it < bound){
				bigArray.at(*it) = reference + tempCounter;
			}
			tempCounter--;
		}
		if (counter + reference > maxChain){
			maxChain = counter + reference;
			chainStart = j+1;
		}
	}
	cout << chainStart << endl;
	cout << maxChain << endl;
}
