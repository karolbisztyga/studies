#include <iostream>
#include <omp.h>
#include <stdlib.h>
#include <time.h>
#include <cmath>
#include <vector>

#define MAX_THREADS 200
#define N 100000
#define MIN 1
#define MAX 1000

using namespace std;

typedef unsigned long long numtype;

numtype random_number(int min = MIN, int max = MAX) {
    return static_cast<numtype>(rand() % max) + min;
}

void print_numbers(const vector<numtype>& numbers) {
    for (size_t i = 0; i < numbers.size(); ++i) {
        cout << numbers[i] << " ";
    }
    cout << endl;
}

void quicksort_mono(vector<numtype>& numbers) {
    if (numbers.size() <= 1) {
        return;
    }
    const size_t pivotIndex = random_number(0, numbers.size());
    vector<numtype> left;
    vector<numtype> right;
    for (size_t i = 0; i < numbers.size(); ++i) {
        if (i == pivotIndex) {
            continue;
        }
        if (numbers[i] < numbers[pivotIndex]) {
            left.push_back(numbers[i]);
        } else {
            right.push_back(numbers[i]);
        }
    }
    quicksort_mono(left);
    quicksort_mono(right);

    const numtype pivot = numbers[pivotIndex];
    numbers.clear();
    numbers.insert(numbers.end(), left.begin(), left.end());
    numbers.push_back(pivot);
    numbers.insert(numbers.end(), right.begin(), right.end());
}



void quicksort_parallel(vector<numtype>& numbers) {
    if (numbers.size() <= 1) {
        return;
    }
    const size_t pivotIndex = random_number(0, numbers.size());
    vector<numtype> left;
    vector<numtype> right;
    for (size_t i = 0; i < numbers.size(); ++i) {
        if (i == pivotIndex) {
            continue;
        }
        if (numbers[i] < numbers[pivotIndex]) {
            left.push_back(numbers[i]);
        } else {
            right.push_back(numbers[i]);
        }
    }

        #pragma omp parallel
        #pragma omp single
        quicksort_parallel(left);
        quicksort_parallel(right);

    const numtype pivot = numbers[pivotIndex];
    numbers.clear();
    numbers.insert(numbers.end(), left.begin(), left.end());
    numbers.push_back(pivot);
    numbers.insert(numbers.end(), right.begin(), right.end());

}

int main() {
    srand (time(NULL));
    // circles and squares
    {
        vector<numtype> numbers_mono;
        vector<numtype> numbers_parallel;
        numbers_mono.reserve(N);
        numbers_parallel.reserve(N);
cout << "generating numbers...";
        for (size_t i = 0; i < N; ++i) {
            auto num = random_number();
            numbers_mono.push_back(num);
            numbers_parallel.push_back(num);
        }
cout << "done\n";
        //print_numbers(numbers_mono);
        
        // monothread
        auto start = omp_get_wtime();
        quicksort_mono(numbers_mono);
        auto end = omp_get_wtime();
        // test if sort is correct
        for (size_t i = 0; i < numbers_mono.size() - 1; ++i) {
            if (numbers_mono[i] > numbers_mono[i+1]) {
                cout << "ERROR: wrong values at index " << i  << ": " 
                    << numbers_mono[i] << "/" << numbers_mono[i+1] << endl;
                return 1;
            }
        }
        cout << "monothread:" << endl;
        //print_numbers(numbers_mono);
        cout << "time elapsed " << end-start << endl;

        // parallel
        start = omp_get_wtime();
        #pragma omp parallel
        #pragma omp single
            quicksort_parallel(numbers_parallel);
        end = omp_get_wtime();
        // test if sort is correct
        for (size_t i = 0; i < numbers_parallel.size() - 1; ++i) {
            if (numbers_parallel[i] > numbers_parallel[i+1]) {
                cout << "ERROR: wrong values at index " << i  << ": " 
                    << numbers_parallel[i] << "/" << numbers_parallel[i+1] << endl;
                return 1;
            }
        }
        cout << "parallel:" << endl;
        //print_numbers(numbers_parallel);
        cout << "time elapsed " << end-start << endl;
    }

    return 0;
}