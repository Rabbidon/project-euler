#include <iostream>
#include <string>
#include <fstream>
#include <list>
using namespace std;

//Sums the scores of all names in te accompanhing file. The rules for scoring can be found at https://projecteuler.net/problem=22
int main(){
	ifstream inFile ("p022_names.txt");
	string line = {};
	getline(inFile,line);

	list<string> names = {};
	string tempString = {};

	for (string::iterator it = line.begin(); it != line.end(); it++){
		if (*it == ','){
			names.push_back(tempString);
			tempString = {};
		}
		if (('A' <= *it) and (*it <= 'Z')){
			tempString.append(string () + *it);
		}
	}

	names.sort();

	int score = 0;
	int counter = 0;

	for (list<string>::iterator it2 = names.begin(); it2 != names.end(); it2++){
		counter ++;
		string givenString = *it2;
		for(string::iterator miniIt = givenString.begin(); miniIt != givenString.end(); miniIt++){
			score += counter*(*miniIt - 'A' + 1);
		}
	}

	cout << score << endl;
	return 0;
}
