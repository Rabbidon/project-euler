#include <iostream>
#include <cmath>
#include <list>
using namespace std;

//Tests primality of every number below a certain bound by checking divisibility of each already discovered prime.
//This could be improved but the number bound required to be tested (2 million) was so small that this ran really quickly.
int main(int argc, char** argv){
	long number = atol(argv[1]);
	list<long> primes;
	long i = 2;
	long total = 0;
        while (i<=number){
                bool primeFlag = 1;
		long b = 0;
                for(list<long>::iterator it=primes.begin(); *it<=sqrt(i) & it!=primes.end(); it++){
                        if (i%*it == 0){
                                primeFlag = 0;
                                break;
                        }
                }
                if (primeFlag){
                        primes.push_back(i);
			total = total + i;
                }
		i++;
        }
        cout << total << endl;
}
