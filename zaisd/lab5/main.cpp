#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <bitset>

typedef unsigned char BYTE;
typedef unsigned long long ULL;

#include "encode.h"
#include "decode.h"

#define MAX_BYTES 0x400

typedef unsigned char BYTE;
typedef unsigned long long ULL;
using namespace std;

int main(int argc, char **argv)
{
	// parsing input file
	if (argc != 2)
	{
		cout << "error, expected: input file\n";
		return 1;
	}
	// init and check file
	ifstream infile(argv[1]);
	if (!infile)
	{
		cout << "error, file " << argv[1] << " not found\n";
		return 1;
	}
	encode(&infile);
	

	return 0;
}
