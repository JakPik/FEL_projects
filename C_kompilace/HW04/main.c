#include <stdio.h>
#include <stdlib.h>

#define ERROR_WRONG_INPUT 100

#define MULTIPLICATION_SYMBOL "x"
#define POWER_SYMBOL "^"

#define LIMIT 1000000   // Highest posible prime number

int Eratosthen_sieve(int limit, int pole[limit + 1]);   
    // Function for finding all prime numbers
int Rewrite_array(int limit, int size, int pole[limit + 1],
                  int prvocisla[size + 1]);
    // Function that creates array of only prime numbers
void input_check(long input, int test); // Tests if the input is correct
void print_line(long input);    // Prints out the base print line
void prime_decomposition_print(int divider, long *number);
    /* Function that writes out prime number decomposition
      with the proper powers of prime numbers */
void print_multiplication(long *previous, long *number);
    /* Checks and prints out multiplication symbol
       if it finds that there could be another prime number */
void prime_number_decomposition(long input, int size, int pole[size + 1]);
    /* Control function that checks through whole prime number array
       and calls coresponding function to test it
       for possible prime number decomposit */
void prime_number_print(long input, int size, int pole[size + 1]);
    /* Checks if the printed number is one or other number
       and calls coresponding print functions */

int main(void) {
    int limit = LIMIT;
    int pole[limit + 1];
    long input = 0;
    int first = 0;  // Help variable to detect first print

    int size = Eratosthen_sieve(limit, pole);
    int prvocisla[size + 1];
    Rewrite_array(limit, size, pole, prvocisla);
    while (1) { // Infinte cycle that is broken out of by input check
        int test = scanf("%ld", &input);
        if (first == 1)
            printf("\n");
        input_check(input, test);
        first = 1;
        prime_number_print(input, size, prvocisla);
    }
    return 0;
}

int Eratosthen_sieve(int limit, int pole[limit + 1]) {
    int count = 0;

    for (int i = 0; i < limit; i++) {     // Inicializes array
        pole[i] = 1;
    }

    for (int i = 2; i * i <= limit; i++) {
        // Filters out multiplications of prime numbers
        if (pole[i]) {
            for (int j = i * i; j <= limit; j += i)
                pole[j] = 0;
        }
    }

    for (int i = 2; i < limit; i++) {   // Writes the prime numbers
        if (pole[i])
            count += 1;
    }
    return count;
}

int Rewrite_array(int limit, int size, int pole[limit + 1],
                  int prvocisla[size + 1]) {
    int position = 0;
    for (int i = 2; i <= limit; i++)
    /* Rewrites the array of primes into more compact array
       of exact size as is number of primes */
        if (pole[i]) {
            prvocisla[position] = i;
            position += 1;
        }
    return 0;
}

void input_check(long input, int test) {
    if ((input < 0) || (test == 0)) {
        fprintf(stderr, "Error: Chybny vstup!\n");
        exit(ERROR_WRONG_INPUT);
    }

    if (input == 0)
        exit(EXIT_SUCCESS);
}

void print_line(long input) {
    printf("Prvociselny rozklad cisla %ld je:\n", input);
}

void prime_decomposition_print(int divider, long *number) {
    long remaining = *number;
    int count = 0;
    if (remaining % divider == 0) {
        printf("%d", divider);
        while (remaining % divider == 0) {
            count += 1;
            remaining = remaining / divider;
        }

        if (count != 1)
            printf(POWER_SYMBOL "%d", count);

        *number = remaining;
    }
    *number = remaining;
}

void print_multiplication(long *previous, long *number) {
    if (*number != *previous) {
        printf(" " MULTIPLICATION_SYMBOL " ");
        *previous = *number;
    }
}

void prime_number_decomposition(long input, int size, int pole[size + 1]) {
    long number = input;
    long previous = input;
    for (int i = 0; i < size; i++) {
        prime_decomposition_print(pole[i], &number);
        if (number == 1)
            break;
        else
            print_multiplication(&previous, &number);
    }
}

void prime_number_print(long input, int size, int pole[size + 1]) {
    if (input == 1) {
        print_line(input);
        printf("%ld", input);
    }
    else {
        print_line(input);
        prime_number_decomposition(input, size, pole);
    }
}
