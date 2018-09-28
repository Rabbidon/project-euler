#include <iostream>
#include <map>
using namespace std;

int main(int argc, char** argv){

	map<int, int> letterMap;

	letterMap[0] = 0;
	letterMap[1] = letterMap[2] = letterMap[6] = letterMap[10] = 3;
	letterMap[4] = letterMap [5] = letterMap[9] = 4;
	letterMap[3] = letterMap[7] = letterMap[8] = letterMap[40] = letterMap[50] = letterMap [60] = 5;
	letterMap[11] = letterMap[12] = letterMap[20] = letterMap[30] = letterMap [80] = letterMap [90] = 6;
	letterMap[15] = letterMap[16] = letterMap[70] = 7;
	letterMap[13] = letterMap[14] = letterMap[18] = letterMap[19] = 8;
	letterMap[17] = 9;

	int total = 0;

	for (int i = atoi(argv[1]); i < atoi(argv[2]); i++){
		if ((i%100)/10 == 1){
			total += letterMap[(i%100)];
		}
		else{
			total += letterMap[10*((i%100)/10)];
			total += letterMap[i%10];
		}
		total += letterMap[i/100] + (i>99)*10 - (i%100 == 0)*3;
	}
	
	cout << total << endl;
	return 0;
}
