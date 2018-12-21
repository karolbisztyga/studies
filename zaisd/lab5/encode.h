#ifndef ENCODE
#define ENCODE

#define MAX_BYTES 0x400
using namespace std;

const size_t chunkSize = 16;

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
	bitset<chunkSize> bits(code);
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
			cout << "error, files over 1KB cannot be handled";
			return;
		}
		++len;
	}
	cout << "file read, size in bytes: " << len << endl;
	for(size_t i = 0;i<len;++i) cout << bytes[i] << " ";cout << endl;
	// sort by occurences
	sort(bytesOccurences.begin(), bytesOccurences.end(), CompareSign());
	// build code table
	string currentCode = "0";
	for (auto it = bytesOccurences.begin(); it != bytesOccurences.end(); ++it) {
		it->code = currentCode;
		currentCode = "1" + currentCode;
	}

	for (auto it = bytesOccurences.begin(); it != bytesOccurences.end(); ++it) {
		cout << it->sign << " -> " << it->occurenecs << ", code: " << it->code << endl;
	}

	// clearing output file
	const string outputFileName = "build/encoded.bin";
	{
		ofstream codedFile(outputFileName, ios::trunc);
	}
	string code = "";
	for (size_t i = 0; i < len; ++i) {
		// find code in code table
		for (auto it = bytesOccurences.begin(); it != bytesOccurences.end(); ++it) {
			if (it->sign == bytes[i]) {
				code += it->code;
				while (code.size() > chunkSize) {
					string codePart = code.substr(0, chunkSize);
					cout << "writing: " << codePart << endl;
					// writing to bin
					writeToBinary(outputFileName, codePart);
					code = code.substr(chunkSize);
				}
				break;
			}
		}
	}
	// writing the stub to bin
	if (code.size() > 0) {
		cout << "*writing " << code << endl;
		writeToBinary(outputFileName, code);
	}
	const string tableFileName = "build/coding_table.txt";
	// writing code table to file
	{
		ofstream file(tableFileName, ios::trunc);
	}
	for (size_t i = 0; i < bytesOccurences.size(); ++i) {
		Sign *sign = &bytesOccurences[i];
		//cout << sign->sign << " " << sign->code << endl;
		string str(1, sign->sign);
		str += sign->code;
		cout << "write: " << str << endl;
		ofstream file(tableFileName, ios::app);
		file << str << endl;
	}

	cout << "encoding done" << endl;
}

#endif