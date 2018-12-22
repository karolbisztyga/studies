#ifndef ENCODE
#define ENCODE

#define MAX_BYTES 0x400
using namespace std;

struct Sign {
	BYTE sign;
	size_t occurenecs;
	string code = "";
};

struct CompareSign {
	bool operator() (const Sign& s1, const Sign& s2) {
		return s2.occurenecs < s1.occurenecs;
	}
};

void writeToBinary(string filename, string code) {
	bitset<CHUNK_SIZE> bits(code);
	unsigned short val = static_cast<unsigned short>(bits.to_ulong());
	ofstream codedFile(filename, ios::app | ios::binary);
	codedFile.write((const char*)&val, sizeof(unsigned short));
}

void encode(ifstream *infile) {
	BYTE bytes[MAX_BYTES];
	vector<Sign> bytesOccurences;
	size_t len = 0;
	// read bytes
	while (*infile >> std::noskipws >> bytes[len]) {
		bool found = false;
		for (auto it = bytesOccurences.begin(); it != bytesOccurences.end(); ++it) {
			if (it->sign == bytes[len]) {
				++it->occurenecs;
				found = true;
				break;
			}
		}
		if (!found) {
			bytesOccurences.push_back({ bytes[len], 1 });
		}
		if (len > MAX_BYTES) {
			cout << "[!] error, files over 1KB cannot be handled";
			return;
		}
		++len;
	}
	cout << "[+] file read, size in bytes: " << len << endl;
	// sort by occurences
	sort(bytesOccurences.begin(), bytesOccurences.end(), CompareSign());
	// build code table
	string currentCode = "0";
	for (auto it = bytesOccurences.begin(); it != bytesOccurences.end(); ++it) {
		it->code = currentCode;
		currentCode = "1" + currentCode;
	}
/*
	for (auto it = bytesOccurences.begin(); it != bytesOccurences.end(); ++it) {
		cout << it->sign << " -> " << it->occurenecs << ", code: " << it->code << endl;
	}
*/
	cout << "[*] writing encoded bytes" << endl;
	// clearing output file
	const string outputFileName = "build/encoded.bin";
	{
		ofstream codedFile(outputFileName, ios::trunc);
	}
	string code = "";
	// writing number of signs that are inserted into file
	{
		unsigned int signCount = static_cast<unsigned int>(len);
		ofstream codedFile(outputFileName, ios::app | ios::binary);
		codedFile.write((const char*)&signCount, sizeof(unsigned int));
	}
	for (size_t i = 0; i < len; ++i) {
		// find code in code table
		for (auto it = bytesOccurences.begin(); it != bytesOccurences.end(); ++it) {
			if (it->sign == bytes[i]) {
				code += it->code;
				while (code.size() > CHUNK_SIZE) {
					string codePart = code.substr(0, CHUNK_SIZE);
					// writing to bin
					writeToBinary(outputFileName, codePart);
					code = code.substr(CHUNK_SIZE);
				}
				break;
			}
		}
	}
	// writing the stub to bin
	if (code.size() > 0) {
		cout << "here in the stub the bytes should be handled the way that the preceding zeroes should be removed if necessary!";
		cout << code << endl;
		writeToBinary(outputFileName, code);
	}
	const string tableFileName = "build/coding_table.txt";
	cout << "[*] write coding table" << endl;
	// writing code table to file
	{
		ofstream file(tableFileName, ios::trunc);
	}
	for (size_t i = 0; i < bytesOccurences.size(); ++i) {
		Sign *sign = &bytesOccurences[i];
		//cout << sign->sign << " " << sign->code << endl;
		string str(1, sign->sign);
		str += sign->code;
		cout << str << endl;
		ofstream file(tableFileName, ios::app);
		file << str << endl;
	}

	cout << "[*] encoding done" << endl;
}

#endif