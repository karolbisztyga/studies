#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <bitset>

typedef unsigned char BYTE;
typedef unsigned long long ULL;

#define CHUNK_SIZE 16

#include "encode.h"
#include "decode.h"

#define MAX_BYTES 0x400

typedef unsigned char BYTE;
using namespace std;

void help() {
	cout << "[*] usage (there are 2 options: encode and decode[e/d])" << endl;
	cout << "[*]   e text_file_path" << endl;
	cout << "[*]   d encoded_file_path coding_table_file_path" << endl;
}

int main(int argc, char **argv)
{
	// parsing input file
	if (argc < 3)
	{
		help();
		return 1;
	}
	if (argv[1][0] != 'd' && argv[1][0] != 'e') {
		help();
		return 1;
	}
	// init and check file
	ifstream infile(argv[2]);
	if (!infile)
	{
		cout << "error, file " << argv[2] << " not found\n";
		return 1;
	}
	if (argv[1][0] == 'e') {
		cout << "encoding" << endl;
		if (argc != 3) {
			help();
			return 1;
		}
		encode(&infile);
	} else if (argv[1][0] == 'd') {
		cout << "decoding" << endl;
		if (argc != 4) {
			help();
			return 1;
		}
		decode(argv[3], &infile);
	}

	return 0;
}
