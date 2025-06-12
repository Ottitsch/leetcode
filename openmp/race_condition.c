// race_condition.c
#include <stdio.h>
#include <omp.h>

int main() {
    int sum = 0;

    #pragma omp parallel for
    for (int i = 0; i < 10000; i++) {
        sum += i; // Race condition
    }

    printf("Sum: %d\n", sum);
    sum = 0;

    //no Race condition
    #pragma omp parallel for reduction(+:sum)
    for (int i = 0; i < 10000; i++) {
        sum += i;
    }
    printf("Sum: %d\n", sum);

    //fixed with critical
    #pragma omp parallel for
    for (int i = 0; i < 10000; i++) {
        #pragma omp critical
        {
            sum += i;
        }
    }

    printf("Sum: %d\n", sum);

    return 0;
}

