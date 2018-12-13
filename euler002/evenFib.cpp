#include <iostream>
#include <stdlib.h>
using namespace std;

/**Generates Fibonacci numbers and sums the even ones. Acutally it could just sum every third term
(patern is odd - odd - even), but for the sake of completeness I did actually manually check each term.
**/
int main(int argc, char** argv){
int cap = atoi(argv[1]);
int int1 = 1;
int int2 = 2;
int sum = 0;
int temp = 0;
while (int1 <= cap){
sum += int1*((int1%2) == 0);
temp = int2;
int2 = int1 + int2;
int1 = temp;
}
cout << sum << endl;
return 0;
}
