#include <stdio.h>

#define ERROR_WRONG_INPUT 100

#define MULTIPLICATION_SYMBOL "x"
#define POWER_SYMBOL "^"

int Eratosthen_sieve(int limit, int pole[limit + 1]);
int Rewrite_array(int limit, int size, int pole[limit + 1],
int prvocisla[size + 1]);
int input_check(int input, int test, int err);
void print_line(int input);
void prime_decomposition_print(int divider, int *number);
void print_multiplication(int *previous, int *number);
void prime_number_decomposition(int input, int size, int pole[size + 1]);
void prime_number_print(int input, int size, int pole[size + 1]);

int main(void) {
    int limit = 1000000;
    int pole[limit + 1];
  int err = 0;
    int input = 1;
  int first = 0;

    int size = Eratosthen_sieve(limit, pole);
    int prvocisla[size + 1];
  Rewrite_array(limit, size, pole, prvocisla);
  while (1) {
    int test = scanf("%d", &input);
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

int Eratosthen_sieve(int limit, int pole[limit + 1]) {
    int count = 0;

  for (int i = 0; i < limit; i++) {
    pole[i] = 1;
  }

  for (int i = 2; i * i <= limit; i++) {
    if (pole[i]) {
      for (int j = i * i; j <= limit; j += i)
        pole[j] = 0;
    }
  }

  for (int i = 2; i < limit; i++) {
    if (pole[i])
      count += 1;
  }
  return count;
}

int Rewrite_array(int limit, int size, int pole[limit + 1],
int prvocisla[size + 1]) {
    int position = 0;
  for (int i = 2; i <= limit; i++)
    if (pole[i]) {
      prvocisla[position] = i;
      position += 1;
    }
  return 0;
}

int input_check(int input, int test, int err) {
  if ((input < 0) || (test == 0)) {
    fprintf(stderr, "Error: Chybny vstup! \n");
    err = ERROR_WRONG_INPUT;
  }
  return err;
}

void print_line(int input) {
  printf("Prvociselny rozklad cisla %d je:\n", input);
}

void prime_decomposition_print(int divider, int *number) {
    int remaining = *number;
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
    // return 0;
  }
  *number = remaining;
  // return 0;
}

void print_multiplication(int *previous, int *number) {
  if (*number != *previous) {
    printf(" " MULTIPLICATION_SYMBOL " ");
    *previous = *number;
  }
}

void prime_number_decomposition(int input, int size, int pole[size + 1]) {
    int number = input;
    int previous = input;
  for (int i = 0; i < size; i++) {
    prime_decomposition_print(pole[i], &number);
    if (number == 1)
      break;
    else
      print_multiplication(&previous, &number);
  }
}

void prime_number_print(int input, int size, int pole[size + 1]) {
  if (input == 1) {
    print_line(input);
    printf("%d", input);
  } else {
    print_line(input);
    prime_number_decomposition(input, size, pole);
  }
}
