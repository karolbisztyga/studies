#include <iostream>
#include <omp.h>

#define MAX_THREADS 200

using namespace std;

double f(double x) {
    return 1.0/(1.0 + x * x);
}

double factorial(double dx, int thread_id, int n_threads) {
    int n = 1/dx;
    double res = 0.0;
    for (size_t i = thread_id; i < n; i += n_threads) {
        res += dx * f(dx * static_cast<double>(i));
    }
    return res;
}

int main() {

    // factorials
    {
        double results[MAX_THREADS];
        for(size_t i = 0; i < MAX_THREADS; ++i) {
            results[i] = 0;
        }
        const double DX = 0.000001;
        auto start = omp_get_wtime();
        #pragma omp parallel// for reduction(+:sum)
        {
            results[omp_get_thread_num()] = factorial(DX, omp_get_thread_num(), omp_get_num_threads());
        }
        auto end = omp_get_wtime();
        double result = 0;
        for(size_t i = 0; i < MAX_THREADS; ++i) {
            result += results[i];
        }
        cout << "factorial " << result*4 << endl;
        cout << "parallel time elapsed   " << end-start << endl;

        start = omp_get_wtime();
        result = factorial(DX, 0, 1);
        end = omp_get_wtime();
        cout << "factorial " << result*4 << endl;
        cout << "monothread time elapsed " << end-start << endl;

        double sum = 0.0;
        start = omp_get_wtime();
        int n = (1/DX);
        #pragma omp parallel for reduction(+:sum)
        for (int i = 0; i < n; ++i)
            sum += DX * f(DX * static_cast<double>(i));
        end = omp_get_wtime();
        cout << "factorial " << sum*4 << endl;
        cout << "parallel for reduction time elapsed " << end-start << endl;
    }
    return 0;
}