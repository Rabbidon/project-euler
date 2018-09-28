#include <iostream>
#include <cmath>
using namespace std;

int main(int argc, char** argv){
	int bound = atoi(argv[1]);
	int partner [bound] = {};
	int sum = 0;
	for (int i = 1; i <= bound; i++){
		partner[i-1] ++;
		for (int j = 2; j <= sqrt(i); j++){
			if (i%j == 0){
				partner[i-1] += j;
				if (j^2 != i){
					partner[i-1] += (i/j);
				}
			}
		}
		cout << partner[i-1] << endl;
	}
	for (int k = 1; k <= bound; k++){
		int buddy = partner[k-1];
		if ((buddy <= bound)and(buddy != k)){
			if (partner[partner[k-1]-1] == k){
				sum += k;
			}
		}
	}
	cout << sum << endl;
	return 0;
}
