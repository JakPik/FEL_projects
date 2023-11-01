#include <stdio.h>

#define ERROR_INTERVAL 100

void positve_evaluate(int a, int *positive, int *negative) {    //Counts quantity of positive and negative numbers
    if (a > 0)
        *positive += 1;
    else if (a < 0)
        *negative += 1;
}

void even_evaluate(int a, int *even, int *odd) {    //Counts quantity of even and odd numbers
    if (a % 2 == 0)
        *even += 1;
    else
        *odd += 1;
}

void max_find(int a, int *max) {    //Compares numbers against max and evaluates its value
    if (a > *max)
        *max = a;
}

void min_find(int a, int *min) {    //Compares numbers against min and evaluates its value
    if (a < *min)
        *min = a;
}

void print_output(int number_sum, int positive_sum, int negative_sum, int even_sum, int odd_sum, int add, int max, int min) {   //Prints out formated output
    printf("\n");
    printf("Pocet cisel: %d\n", number_sum);
    printf("Pocet kladnych: %d\n", positive_sum);
    printf("Pocet zapornych: %d\n", negative_sum);
    printf("Procento kladnych: %0.2f\n", positive_sum / (number_sum / 100.0f));     //Calcualtes percentage value
    printf("Procento zapornych: %0.2f\n", negative_sum / (number_sum / 100.0f));    //Calcualtes percentage value
    printf("Pocet sudych: %d\n", even_sum);
    printf("Pocet lichych: %d\n", odd_sum);
    printf("Procento sudych: %0.2f\n", even_sum / (number_sum / 100.0f));           //Calcualtes percentage value
    printf("Procento lichych: %0.2f\n", odd_sum / (number_sum / 100.0f));           //Calcualtes percentage value
    printf("Prumer: %0.2f\n", add / (number_sum * 1.0f));                           //Calcualtes average value
    printf("Maximum: %d\n", max);
    printf("Minimum: %d\n", min);
}

int calcualtion(int *number, int *number_sum, int *add, int *positive_sum, int *negative_sum, int *even_sum, int *odd_sum, int *max, int *min) {
/*
For each number calls calculation, it also prints out all read numbers
*/
    printf("%d", *number);
    *number_sum += 1;
    *add += *number;
    positve_evaluate(*number, &*positive_sum, &*negative_sum);
    even_evaluate(*number, &*even_sum, &*odd_sum);
    max_find(*number, &*max);
    min_find(*number, &*min);
    return 1;
}

int main(void) {
    int number;
    int err = 0;
    int first_done = 0;
    
    int number_sum = 0;
    int positive_sum = 0;
    int negative_sum = 0;
    int even_sum = 0;
    int odd_sum = 0;
    int max = -10000;
    int min = 10000;
    int add = 0;

    while (scanf("%d", &number) != EOF) {   //Runs for as long as there is something on the input
        if (number < -10000 || number > 10000) {
            err = ERROR_INTERVAL;
            printf("\n");
            printf("Error: Vstup je mimo interval!\n");
            return err;
        } 
        else {
            if (first_done == 1)
                printf(", ");
            first_done = calcualtion(&number, &number_sum, &add, &positive_sum, &negative_sum, &even_sum, &odd_sum, &max, &min);
        }
    }
    print_output(number_sum, positive_sum, negative_sum, even_sum, odd_sum, add, max, min);
    return err;
}
