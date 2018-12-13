#include <iostream>
using namespace std;

//There exists exactly one Pythagorean triple a,b,c s.t. a+b+c = 1000.
//This script finds it efficiently.
int main(){
	// We iterate over values of a, and then use binary search on the possible values of b (and set c=1000-a-b)
	// to find the critical point at which a^2+b^2 becomes greater than c^2. We keep going until we find a solution.
	// 1000 is hard-coded in here, but this could easily be genertalised to any n - we just need to add in an escape clause.
	// In this case the runtime is O(n*log(n)).
	for (int a = 1; a<1000; a++)
	{
		int bmin = 1;
		int bmax = 1000;
		int b = (bmax+bmin)/2
		//The binary search portion.
		while (b>bmin)
		{
			if (a*a + b*b > c*c)
			{
				bmax = b;
				b = (bmax+bmin)/2;
			}
			else if (a*a + b*b < c*c)
			{
				bmin = b;
				b = (bmax+bmin)/2;
			}
			else 
			{
				cout << a << endl;
				cout << b << endl;
				cout << c << endl;
			}
		}
	}
}