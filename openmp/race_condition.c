#include <stdio.h>
#include <omp.h>

#define N 10000000
#define TRIALS 10

int main() {
    double start, end;
    int sum;

    // 1. Naive version (with race condition)
    printf("== Naive version (Race Condition) ==\n");
    for (int t = 0; t < TRIALS; t++) {
        sum = 0;
        start = omp_get_wtime();

        #pragma omp parallel for
        for (int i = 0; i < N; i++) {
            sum += i; // Race condition
        }

        end = omp_get_wtime();
        printf("Trial %d: Sum = %d, Time = %f s\n", t+1, sum, end - start);
    }

    // 2. Reduction version (correct and efficient)
    printf("\n== Reduction version ==\n");
    for (int t = 0; t < TRIALS; t++) {
        sum = 0;
        start = omp_get_wtime();

        #pragma omp parallel for reduction(+:sum)
        for (int i = 0; i < N; i++) {
            sum += i;
        }

        end = omp_get_wtime();
        printf("Trial %d: Sum = %d, Time = %f s\n", t+1, sum, end - start);
    }

    // 3. Critical version (correct but slower)
    printf("\n== Critical section version ==\n");
    for (int t = 0; t < TRIALS; t++) {
        sum = 0;
        start = omp_get_wtime();

        #pragma omp parallel for
        for (int i = 0; i < N; i++) {
            #pragma omp critical
            {
                sum += i;
            }
        }

        end = omp_get_wtime();
        printf("Trial %d: Sum = %d, Time = %f s\n", t+1, sum, end - start);
    }

    return 0;
}

