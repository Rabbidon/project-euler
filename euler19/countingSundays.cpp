#include <iostream>
#include <map>
using namespace std;

int main(){

	int sundays = 0;
	int day = 6;

	map<int, int> monthMap;

	monthMap[0] = 31;
	monthMap[1] = 31;
	monthMap[2] = 28;
	monthMap[3] = 31;
	monthMap[4] = 30;
	monthMap[5] = 31;
	monthMap[6] = 30;
	monthMap[7] = 31;
	monthMap[8] = 31;
	monthMap[9] = 30;
	monthMap[10] = 31;
	monthMap[11] = 30;

	for (int i = 1; i <= 1200; i++){
		day = (day+monthMap[(i-1)%12])%7;
		if ((i-1)%48 == 38){
			day = (day + 1)%7;
		}
		if (day == 0){
			sundays ++;
		}
	}
	cout << sundays << endl;
	return 0;
}
