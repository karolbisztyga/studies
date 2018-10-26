#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
// used for std::sort on vector
#include <algorithm>

using namespace std;

const int INFINITY = static_cast<unsigned int>(-1)/2;

struct Edge
{
	size_t from;
	size_t to;
	int weight;
};

void printNodes(map<size_t, int>& nodes)
{
	cout << "Nodes: " << endl;
	for(auto it = nodes.begin(); it != nodes.end(); ++it)
	{
		cout << "[id: " << it->first << ", total weight: " << it->second << "]" << endl;
	}
	cout << endl;
}

/**
	algorithm:
	1. find an increasing path
	2. find the value of the smallest capacity in this path
	3. increase each path and total flow
	repeat those steps until increasing path cannot be found
	* backward flow - if there is enough points on the edge we can go backwards and substract from it
*/

bool maxFlowMatrix(vector<vector<int>>& neighbours, map<size_t, int>& nodes)
{
	bool increasingPathFound = false;
	int totalFlow = 0;
	do {
		increasingPathFound = false;
		// 1. find an increasing path
		cout << "checking for increasing path" << endl;
		size_t currNode = 0;
		set<size_t> path = { 0 };
		while (currNode != neighbours.size() - 1)
		{
			cout << "current node: " << currNode << endl;
			bool nextNodeFound = false;
			for(size_t i=0;i<neighbours[currNode].size();++i)
			{
				cout << neighbours[currNode][i] << " " ;
				if (neighbours[currNode][i] != 0) 
				{
					// found next node
					currNode = i;
					path.insert(currNode);
					nextNodeFound = true;
					break;
				}
				// handle backward flow
				//if (neighbours[i][currNode] != 0 && ...[enough points ...])
			}
			cout << endl;
			if (!nextNodeFound)
			{
				// if no next node was found, there is no increasing path
				increasingPathFound = false;
				break;
			}
		}
		// increasing path found if we end up searching for it in the final node
		if (currNode == neighbours.size() - 1)
		{
			increasingPathFound = true;
			// 2. find the value of the smallest capacity in this path
		}
	} while(increasingPathFound);
	return false;
}

bool maxFlowList(vector<Edge>& edges, map<size_t, int>& nodes)
{
	return false;
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
	bool result = false;
	map<size_t, int> nodes;
	if (algorithm == 'm')
	{
		vector<vector<int>> weights;
		size_t size = 0;
		infile >> size;
		cout << "read matrix of size " << size << endl;
		weights.resize(size);
		for (size_t i = 0; i < size; ++i)
		{
			weights[i].resize(size);
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
		for (size_t i = 0; i < size ; ++i)
		{
			nodes[i] = INFINITY;
		}
		nodes[0] = 0;
		result = maxFlowMatrix(weights, nodes);
	}
	else
	{
		vector<Edge> edges;
		// parsing file
		do
		{
			Edge edge;
			edges.push_back(edge);
		} while(infile >> edges.back().from && infile >> edges.back().to && infile >> edges.back().weight);
		edges.pop_back();
		sort(edges.begin(), edges.end(), [](const Edge &e1, const Edge &e2) {
			return e1.from < e2.from;
		});
		cout << "edges:" << endl;
		for (size_t i = 0; i < edges.size(); ++i)
		{
			cout << edges.at(i).from << " " << edges.at(i).to << " " << edges.at(i).weight << endl;
		}
		for(size_t i = 0; i < edges.size(); ++i)
		{
			nodes[edges[i].from] = INFINITY;
			nodes[edges[i].to] = INFINITY;
		}
		nodes[0] = 0;
		result = maxFlowList(edges, nodes);
	}
	if (!result)
	{
		cout << "error, algorithm failed\n";
        return 1;
	}
	cout << "shortest paths: " << endl;
	printNodes(nodes);
	return 0;
}
