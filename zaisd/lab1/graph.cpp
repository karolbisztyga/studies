#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

// find shortest path using matrix of neighbours
int shortestPathMatrix(vector<vector<int>>& neighbours)
{
	return 0;
}

// find shortest path using list of edges
struct Edge
{
	size_t from;
	size_t to;
	int weight;
};

int shortestPathList(vector<Edge>& edges)
{
	return 0;
}

int main(int argc, char **argv)
{
	// parsing input file
	if (argc != 3)
	{
		cout << "error, expected: input file and algorithm(m-matrix, l-list)\n";
		return 1;
	}
	// init and check file
	std::ifstream infile(argv[1]);
	if (!infile)
	{
		cout << "error, file " << argv[1] << " not found\n";
		return 1;
	}
	// check algorithm
	const char algorithm = argv[2][0];
	if (algorithm != 'm' && algorithm != 'l')
	{
		cout << "error, wrong algorithm(must be 'm' for matrix or 'l' for list)\n";
		return 1;
	}
	int *result = nullptr;
	if (algorithm == 'm')
	{
		vector<vector<int>> weights;
		size_t size = 0;
		infile >> size;
		cout << "read matrix of size " << size << endl;
		weights.reserve(size);
		for (size_t i = 0; i < size; ++i)
		{
			weights[i].reserve(size);
		}
		// parsing file
		for (size_t i = 0; i < size; ++i)
		{
			for (size_t j = 0; j < size; ++j)
			{
				infile >> weights[i][j];
			}
		}
		// print matrix
		for (size_t i = 0; i < size; ++i)
		{
			for (size_t j = 0; j < size; ++j)
			{
				cout << weights[i][j] << " ";
			}
			cout << endl;
		}
		// perform algorithm
		result = new int(shortestPathMatrix(weights));
	}
	else
	{
		vector<Edge> edges;
		// parsing file
		while(1)
		{
		}
		result = new int(shortestPathList(edges));
	}
	if (result == nullptr)
	{
		cout << "error, algorithm failed\n";
	}
	cout << "shortest path: " << *result << endl;
	free(result);
	return 0;
}