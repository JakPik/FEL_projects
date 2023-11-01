#include <stdio.h>

#define ERROR_WRONG_INPUT 100

#define MULTIPLICATION_SYMBOL "x"
#define POWER_SYMBOL "^"

long Eratosthen_sieve(long limit, long pole[limit + 1]);
long Rewrite_array(long limit, long size, long pole[limit + 1],
                   long prvocisla[size + 1]);
int input_check(long input, int test, int err);
void print_line(long input);
void prime_decomposition_print(long divider, long *number);
void print_multiplication(long *previous, long *number);
void prime_number_decomposition(long input, long size, long pole[size + 1]);
void prime_number_print(long input, long size, long pole[size + 1]);

int main(void) {
  long limit = 1000000;
  long pole[limit + 1];
  int err = 0;
  long input = 1;
  int first = 0;

  long size = Eratosthen_sieve(limit, pole);
  long prvocisla[size + 1];
  Rewrite_array(limit, size, pole, prvocisla);
  while (1) {
    int test = scanf("%ld", &input);
    if (first == 1)
      printf("\n");
    if (input_check(input, test, err) != 0)
      return err;
    if (input == 0)
      break;
    first = 1;
    prime_number_print(input, size, prvocisla);
  }
  return 0;
}

long Eratosthen_sieve(long limit, long pole[limit + 1]) {
  long count = 0;

  for (long i = 0; i < limit; i++) {
    pole[i] = 1;
  }

  for (long i = 2; i * i <= limit; i++) {
    if (pole[i]) {
      for (long j = i * i; j <= limit; j += i)
        pole[j] = 0;
    }
  }

  for (long i = 2; i < limit; i++) {
    if (pole[i])
      count += 1;
  }
  return count;
}

long Rewrite_array(long limit, long size, long pole[limit + 1],
                   long prvocisla[size + 1]) {
  long position = 0;
  for (long i = 2; i <= limit; i++)
    if (pole[i]) {
      prvocisla[position] = i;
      position += 1;
    }
  return 0;
}

int input_check(long input, int test, int err) {
  if ((input < 0) || (test == 0)) {
    fprintf(stderr, "Error: Chybny vstup! \n");
    err = ERROR_WRONG_INPUT;
  }
  return err;
}

void print_line(long input) {
  printf("Prvociselny rozklad cisla %ld je:\n", input);
}

void prime_decomposition_print(long divider, long *number) {
  long remaining = *number;
  long count = 0;
  if (remaining % divider == 0) {
    printf("%ld", divider);
    while (remaining % divider == 0) {
      count += 1;
      remaining = remaining / divider;
    }
    if (count != 1)
      printf(POWER_SYMBOL "%ld", count);
    *number = remaining;
    // return 0;
  }
  *number = remaining;
  // return 0;
}

void print_multiplication(long *previous, long *number) {
  if (*number != *previous) {
    printf(" " MULTIPLICATION_SYMBOL " ");
    *previous = *number;
  }
}

void prime_number_decomposition(long input, long size, long pole[size + 1]) {
  long number = input;
  long previous = input;
  for (long i = 0; i < size; i++) {
    prime_decomposition_print(pole[i], &number);
    if (number == 1)
      break;
    else
      print_multiplication(&previous, &number);
  }
}

void prime_number_print(long input, long size, long pole[size + 1]) {
  if (input == 1) {
    print_line(input);
    printf("%ld", input);
  } else {
    print_line(input);
    prime_number_decomposition(input, size, pole);
  }
}
