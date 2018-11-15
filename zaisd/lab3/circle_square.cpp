#include <iostream>
#include <omp.h>
#include <vector>
#include <stdlib.h>
#include <time.h>
#include <cmath>

#define MAX_THREADS 200
#define NUM_POINTS 100000000
#define R 5
#define DECIMAL_PLACES 3

using namespace std;

struct Point {
    double x = 0;
    double y = 0;
};

double random_coordinate() {
    const size_t POW = static_cast<size_t>(pow(10, DECIMAL_PLACES));
    return (static_cast<double>(rand() % (R * 2 * POW)) / POW) - R;
}

bool is_in_circle(Point& point) {
//cout << point.x*point.x << " + " << point.y*point.y << " <= " << R*R << endl;
    return ((point.x*point.x + point.y*point.y) <= R*R);
}

int main() {
    srand (time(NULL));
    // circles and squares
    {
        vector<Point> points;
        points.reserve(NUM_POINTS);
        for (size_t i = 0; i < NUM_POINTS; ++i) {
            points[i] = { random_coordinate(), random_coordinate() };
//cout << points[i].x << ", " << points[i].y << endl;
        }

        // monothread
        size_t points_in_circle = 0;
        auto start = omp_get_wtime();
        for (size_t i = 0; i < NUM_POINTS; ++i) {
            if (is_in_circle(points[i])) {
                ++points_in_circle;
            }
        }
        auto end = omp_get_wtime();
        cout << "monothread:" << endl;
        cout << "points in circle: " << points_in_circle << " / " << 
            NUM_POINTS << endl;
        cout << "time elapsed " << end-start << endl;
        double PI = 4 * ( static_cast<double>(points_in_circle) / 
            static_cast<double>(NUM_POINTS) );
        cout << "PI: " << PI << endl;

        points_in_circle = 0;
        // parallel
        start = omp_get_wtime();
        #pragma omp parallel for reduction(+:points_in_circle)
            for (size_t i = 0; i < NUM_POINTS; ++i) {
                if (is_in_circle(points[i])) {
                    ++points_in_circle;
                }
            }
        end = omp_get_wtime();
        cout << "parallel:" << endl;
        cout << "points in circle: " << points_in_circle << " / " << 
            NUM_POINTS << endl;
        cout << "time elapsed " << end-start << endl;
        PI = 4 * ( static_cast<double>(points_in_circle) / 
            static_cast<double>(NUM_POINTS) );
        cout << "PI: " << PI << endl;
    }
    // jest kolo wpisane w kwadrat
    // wygenerowac n punktow(np 1 000 000)
    // sprawdzic ktore sie mieszcza w kole
    /**
        pole kw/pole kola = 4r*r/PI * r * r
        czyli PI = 4 * (pole kola/pole kw)
        i wyliczyc to PI na podstawie stosunku punktow ktore sa w kole(pole kola)
        i wszystkich(pole kw)
        
        zrobic to monothread i parallel i zmierzyc czas
    */

    return 0;
}