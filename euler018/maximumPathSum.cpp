#include <iostream>
using namespace std;

//Takes a pyramidal array and returns the maximum sum of elements along a path from top to bottom.
//Uses basic dynamic programming.
int main(int argc, char** argv){
	int depth = atoi(argv[1]);
	if ((depth*(depth + 1))/2 != argc - 2){
		cout << "You fucked up" << endl;
		return 0;
	}
	int elementNumber = argc - 2;
	int triangle [elementNumber];
	for (int i = 0; i < elementNumber; i++){
		triangle[i] = atoi(argv[i + 2]);
	}
	for (int j = depth - 1; j > 0; j--){
		for (int k = (j*(j-1))/2; k < (j*(j+1))/2; k++){
			triangle[k] += max(triangle[k + j], triangle[k + j + 1]);
		}
	}

	cout << triangle[0] << endl;
	return 0;
	}
