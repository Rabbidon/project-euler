#include <iostream>
#include <array>
using namespace std;

//Given a grid of numbers, calculates 
int main(int argc, char** argv){
	//Arguments are the grid in line form, and the grid dimensions.
	int line = atoi(argv[1]);
	int height = atoi(argv[2]);
	int width = atoi(argv[3]);
	if (!(height*width == argc - 4)){
		cout << "" << endl;
		return 0;
	}

	//Recreates the grid structure from the input.
	int grid [height][width];
	for (int i=0; i<height; i++){
		for (int j=0; j<width; j++){
			grid[i][j] = atoi(argv[3 + i*width + j]);
		}
	}
	int maxProd = 0;
	int prod = 1;
	//Checks every possible vertical, horizontal, and diagonal product of four digits.
	for (int a=0; a<height; a++){
                for (int b=0; b<=(width-line); b++){
			prod = 1;
                        for (int c=0; c<line; c++){
                                prod = prod*grid[a][b+c];
                                if (prod > maxProd){
                                        maxProd = prod;
                                }
                        }
                }
        }
	for (int a=0; a<=(height-line); a++){
                for (int b=0; b<width; b++){
			prod = 1;
                        for (int c=0; c<line; c++){
                                prod = prod*grid[a+c][b];
                                if (prod > maxProd){
                                        maxProd = prod;
                                }
                        }
                }
        }

	for (int a=0; a<=(height-line); a++){
		for (int b=0; b<=(width-line); b++){
			prod = 1;
			for (int c=0; c<line; c++){
				prod = prod*grid[a+c][b+c];
				if (prod > maxProd){
					maxProd = prod;
				}
			}
		}
	}
	for (int a=0; a<=(height-line); a++){
                for (int b=width-1; b>=line-1; b--){
			prod = 1;
                        for (int c=0; c<line; c++){
                                prod = prod*grid[a+c][b-c];
                                if (prod > maxProd){
                                        maxProd = prod;
                                }
                        }
                }
        }

	cout << maxProd << endl;
	return 0;
}
