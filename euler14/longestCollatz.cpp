#include <iostream>
#include <list>
#include <vector>
#include <assert.h>
using namespace std;


//A Collatz sequence is defined as follows: a_(i+1) = (a_i)/2 if a_i is even, a_(i+1) = 3*(a_i) + 1 if a_i is odd.
//It terminates at 1.
//The task given is to find the starting number under one million that produces the longest sequence.
int main(int argc, char** argv){
	int bound = atoi(argv[1]);
	vector<int> bigArray;
	bigArray.push_back(1);
	for (int i = 1; i < bound; i++){
		bigArray.push_back(0);
	}
        int maxChain = 1;
	int chainStart = 1;

	//Generates step-by-step a Collatz sequence starting at each number, keeping track of how long the sequnce is.
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
				//If we come across a number we have seen before, then we have already calculated how many steps till
				//termination from here, so we break and just write in the number of steps for all the previous elements based on this knowlege.
				if (bigArray.at(position) != 0){
					break;
				}
			}
		}
		int counter = elementList.size();
		int tempCounter = counter;
		int reference = bigArray.at(position);
		//Filling in number of steps required for all elements we haven't seen before.
		for (list <long long>::iterator it = elementList.begin(); it != elementList.end(); it++){
			if (*it < bound){
				bigArray.at(*it) = reference + tempCounter;
			}
			tempCounter--;
		}
		//If the chain length exceeds the previous longest chain length, we note the new length and the starting point.
		if (counter + reference > maxChain){
			maxChain = counter + reference;
			chainStart = j+1;
		}
	}
	cout << chainStart << endl;
	cout << maxChain << endl;
}
