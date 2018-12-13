#include <iostream>
#include <map>
using namespace std;


//Program to find how many times the first of the month fell on a Sunday during (1900,2000].
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

	//Loop that works out the first day of each month iteratively, using the previous first day and number of days in the current month.
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
