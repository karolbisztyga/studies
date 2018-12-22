#ifndef DECODE
#define DECODE

#include <map>

void decode(char *binfile_path, ifstream *infile_table) {
	// reading coding table
	string line = "";
	cout << "reading coding table" << endl;
	map<string, char> codingTable;
	while(getline(*infile_table, line)) {
		char sign = line[0];
		codingTable[line.substr(1)] = sign;
		cout << line.substr(1) << " -> " << codingTable[line.substr(1)] << endl;
	}
	// handling binary
	cout << "check file " << binfile_path << endl;
	ifstream infile(binfile_path, ios::binary);
	if (!infile)
	{
		cout << "error, file " << binfile_path << " not found\n";
		return;
	}
	unsigned short data;
	string decodedText = "";
	string buffer = "";
	while(infile.read((char*)&data, sizeof(data))) {
		cout << data;
		string str = bitset<CHUNK_SIZE>(data).to_string();
		cout << " -> " << str << endl;
		// decoding meanwhile
		bool signDecoded = false;
		buffer += str;
		/*do {
			signDecoded = false;
			// try to decode single sign
			for(size_t i = 1; i < buffer.size(); ++i) {
				cout << "trying to find in coding table: " << buffer.substr(0, i) << endl;
				if (codingTable.find(buffer.substr(0, i)) != codingTable.end()) {
					cout << "found" << buffer.substr(0, i) << endl;
					char decodedChar = codingTable[buffer.substr(0, i)];
					cout << "decoded: " << buffer.substr(0, i) << " -> " << decodedChar << endl;
					decodedText.push_back(decodedChar);
					buffer = buffer.substr(i);
					signDecoded = true;
					break;
				}
			}
		} while(signDecoded);*/
	}
	cout << "decoded text: " << decodedText << endl;
}

#endif