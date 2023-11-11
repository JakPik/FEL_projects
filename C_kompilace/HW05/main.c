#include <stdio.h>
#include <stdlib.h>

#define ERROR_INPUT 100
#define ERROR_WRONG_SIZE 101
#define ERROR_REALLOCATION 102

#define INIT_LIMIT 1
#define UPPER_ALP_BEGINNING 65
#define UPPER_ALP_END 90
#define LOWER_ALP_BEGINNING 97
#define LOWER_ALP_END 122
#define EMPTY_SPACE 6
#define NUMBER_OF_PEERMUTATIONS 52

void input_test(char input, char *str); // Tests if the input is letter
void length_test(int first, int second);
    /* Tests if two strings
       are the same length */
void *my_realloc(void *ptr, size_t size);   // Reallocs string to larger size
void realloc_test(char *str);   // Tests if reallocation happened succesfully
char *read_line(int *size); // Function that reads string and counts its length
void permutate_text(char *permutate, int size, int permutation);
    // Runs permutation of the whole string
int compare(char *permutate, const char *heard, int size);
    // Compares permutated string with the one heard
int find_permutation(int *similar);
    /* Finds the value of how much the letters must be permutated
       to give correct answer */
int shift(const char *heard, const char *str, int size);
    /* Control function that calls other functions
       to correctly decipher Caesar cipher */
void print_result(char *cipher, int permutation, int size);
    // Prints the corect permutated answer

int main(void) {
    int size = 0;
    char *cipher = read_line(&size);
    char *heard = read_line(&size);
    int permutation = shift(&*heard, &*cipher, size);
    print_result(&*cipher, permutation, size);
    return 0;
}

void input_test(char input, char *str) {
    if (input < UPPER_ALP_BEGINNING) {  
        // Test for char being below ASCII value of 'A'
        fprintf(stderr, "Error: Chybny vstup!\n");
        free(str);
        exit(ERROR_INPUT);
    } else if (input > UPPER_ALP_END) {
        // Test for char being above ASCII value of 'Z'
        if (input < LOWER_ALP_BEGINNING || input > LOWER_ALP_END) {
            // Test for char being below ASCII value of 'a' and above 'z'
            free(str);
            fprintf(stderr, "Error: Chybny vstup!\n");
            exit(ERROR_INPUT);
        }
    }
}

void length_test(int first, int second) {
    if (first != second) {
        fprintf(stderr, "Error: Chybna delka vstupu!\n");
        exit(ERROR_WRONG_SIZE);
    }
}

void *my_realloc(void *ptr, size_t size) {
    void *ret = realloc(ptr, size);
    realloc_test(*&ret);
    return ret;
}

void realloc_test(char *str) {
    if (str == NULL) {
        fprintf(stderr, "Error: Chyba realokace!\n");
        free(str);
        exit(ERROR_REALLOCATION);
    }
}

char *read_line(int *size) {
    int capacity = INIT_LIMIT;
    char *str = my_realloc(NULL, capacity);
    int len = 0;
    int c;
    while ((c = getchar()) != EOF && c != '\n') {
        input_test(c, &*str);
        if (len == capacity) {
            capacity *= 2;
            str = my_realloc(str, sizeof(char) * (capacity + 1));
        }
        str[len++] = c;
    }

    if (len > 0) {
        str[len] = '\0';
    } else {
        free(str);
        str = NULL;
    }

    if (*size == 0) {
        *size = len;
    }
    else {
        length_test(*size, len);
    }
    return str;
}

void permutate_text(char *permutate, int size, int permutation) {
    for (int i = 0; i < size; i++) {
        if (permutate[i] + permutation > LOWER_ALP_END) {
                permutate[i] = UPPER_ALP_BEGINNING +
            (permutate[i] + permutation- LOWER_ALP_END - 1);
        } else if (permutate[i] + permutation > UPPER_ALP_END &&
                permutate[i] < LOWER_ALP_BEGINNING) {
            permutate[i] = permutate[i] + EMPTY_SPACE + permutation;
        } else {
            permutate[i] = permutate[i] + permutation;
        }
    }
}

int compare(char *permutate, const char *heard, int size) {
    int same_check = 0;
    int permutation = 1;
    permutate_text(&*permutate, size, permutation);

    for (int i = 0; i < size; i++) {
        if (permutate[i] == heard[i]) {
            same_check += 1;
        }
    }
    return same_check;
}

int find_permutation(int *similar) {
    int max_compare = 0;
    int index = 0;

    for (int i = 0; i < NUMBER_OF_PEERMUTATIONS; i++) {
        if (similar[i] > max_compare) {
            max_compare = similar[i];
            index = i;
        }
    }
    return (index + 1) % NUMBER_OF_PEERMUTATIONS;
}

int shift(const char *heard, const char *str, int size) {
    int similar[NUMBER_OF_PEERMUTATIONS];
    char *permutate = realloc(NULL, size);

    for (int i = 0; i < size; i++)
        permutate[i] = str[i];

    for (int i = 0; i < NUMBER_OF_PEERMUTATIONS; i++) {
        similar[i] = compare(permutate, heard, size);
    }
    int index = find_permutation(&*similar);
    return index;
}

void print_result(char *cipher, int permutation, int size) {
    permutate_text(&*cipher, size, permutation);

    for (int i = 0; i < size; i++) {
        printf("%c", cipher[i]);
    }
    printf("\n");
}
