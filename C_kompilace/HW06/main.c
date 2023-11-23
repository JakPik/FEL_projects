#include <stdio.h>
#include <stdlib.h>

#define ERROR_INPUT 100
#define ERROR_REALLOCATION 101

#define MULTIPLICATION '*'
#define ADD '+'
#define SUBTRACT '-'

void input_test(int input);
// Test if the input is read correctly

int *matrix_make(int row, int column, int operation);
// Creates matrix of exact number of rows and columns

void matrix_compatibility(int *matrix_A, int *matrix_B, char operation);
// Checks if the matrixes are compatible for the cuirrent opperation

void read_matrix(int *matrix);
// Function for printing out matrix

void clear_matrix_memory(int *matrix);
/* When new operational matrix is created
   this function clears its values in memory */

int *matrix_multiplication(int *matrix_A, int *matrix_B, int idx);
// Function that multiplies two matrixes

int *matrix_add(int *matrix_A, int *matrix_B, int idx);
// Function that adds two matrixes

void adjust_matrix_array(int **matrix_array, int *size);
// Moves the matrixes in array closer to idx 0

void adjust_operations(char *operations, int size);
// Moves operation in arraz closer to idx 0

int *matrix_calculation(int **matrix_array, char *operations,
                        int number_of_matrixes);
// Control function that determins what will be done with the matrixes

int **reallocation_matrix_array(int **matrix_array, int number_of_matrixes,
                                int used);
// Function to realocate matrix array and clear all new memory

int *reallocation_matrix(int matrix_size);
// Function to realocate matrix and clear all new memory

char *reallocation_operation(char *operation, int number_of_matrixes, int used);
// Function to realocate operations array and clear all new memory

int main(void) {
    int open_input = 1;
    // Help variable to determin when to stop the cycle

    int idx = 0; // Variable to index each new matrix and operation into array
    int row = 0;
    int column = 0;
    int number_of_matrixes = 4; // Default value of predicted number matrixes
    int created_matrixes = 0;   // Total count of actualy created matrixes
    int **matrix_array = reallocation_matrix_array(NULL, number_of_matrixes, 0);
    // Array of matrixes
    char *operations = reallocation_operation(NULL, number_of_matrixes, 0);
    // Array of operations
    char operation_check = '0';
    
    while (open_input == 1) {
        if (created_matrixes++ >= number_of_matrixes) {
        // Checks if the arrays need to be reallocated
        number_of_matrixes = number_of_matrixes * 2;
        matrix_array = reallocation_matrix_array(
            *&matrix_array, number_of_matrixes, created_matrixes);

        operations = reallocation_operation(*&operations, number_of_matrixes,
                                            created_matrixes);
        }

        input_test(scanf("%d", &row));
        input_test(scanf("%d", &column));
        if(operation_check == SUBTRACT) {
            matrix_array[idx] = matrix_make(row, column, -1);
            operations[idx - 1] = ADD;
        }
        else {
            matrix_array[idx] = matrix_make(row, column, 1);
        }

        getchar();
        operation_check = '0';
        input_test(scanf("%c", &operation_check));
        operations[idx] = operation_check;
        switch (operation_check) {
            case MULTIPLICATION:
            case ADD:
            case SUBTRACT:
                break;
            default:
                operations[idx] = '0';
                open_input = 0;
                break;
        }

        idx += 1;
    }

    int *final_matrix =
        matrix_calculation(*&matrix_array, *&operations, created_matrixes);

    printf("%d %d\n", final_matrix[0], final_matrix[1]);
    read_matrix(final_matrix);

    free(operations);
    free(matrix_array[0]);
    free(matrix_array);
    return 0;
}

int **reallocation_matrix_array(int **matrix_array, int number_of_matrixes,
                                int used) {
    int **new_matrix =
        (int **)realloc(matrix_array, sizeof(int *) * number_of_matrixes);
    if (new_matrix == NULL) {
        fprintf(stderr, "ERROR: Wrong allocation\n");
        exit(ERROR_REALLOCATION);
    }

    for (int i = used; i < number_of_matrixes; i++) {
        new_matrix[i] = NULL;
    }

    return new_matrix;
}

int *reallocation_matrix(int matrix_size) {
    int *new_matrix = (int *)malloc(matrix_size * sizeof(int) + 2 * sizeof(int));
    if (new_matrix == NULL) {
        fprintf(stderr, "ERROR: Wrong allocation\n");
        exit(ERROR_REALLOCATION);
    }

    for (int i = 0; i < matrix_size + 2; i++) {
        new_matrix[i] = 0;
    }

    return new_matrix;
}

char *reallocation_operation(char *operation, int number_of_matrixes,
                             int used) {
    char *new_opperations =
        (char *)realloc(operation, sizeof(char) * number_of_matrixes);
    if (new_opperations == NULL) {
        fprintf(stderr, "ERROR: Wrong allocation\n");
        exit(ERROR_REALLOCATION);
    }

    for (int i = used; i < number_of_matrixes; i++) {
        new_opperations[i] = '0';
    }

    return new_opperations;
}

void input_test(int input) {
    if (input == 0) {
        fprintf(stderr, "Error: Chybny vstup!\n");
        exit(ERROR_INPUT);
    }

    if (input == ERROR_INPUT) {
        fprintf(stderr, "Error: Chybny vstup!\n");
        exit(ERROR_INPUT);
    }
}

int *matrix_make(int row, int column, int operation) {
    int input;
    int *matrix = reallocation_matrix(column * row);
    matrix[0] = row;
    matrix[1] = column;

    for (int i = 0; i < row; i++) {
        for (int j = 0; j < column; j++) {
        input_test(scanf("%d", &input));
        matrix[i * column + j + 2] = input * operation;
        }
    }

    return matrix;
}

void matrix_compatibility(int *matrix_A, int *matrix_B, char operation) {
    switch (operation) {
    // Switches between coresponding control based on operation
    case MULTIPLICATION:
        if (matrix_A[1] != matrix_B[0]) {
        input_test(ERROR_INPUT);
        }
        break;
    case ADD:
        if (matrix_A[0] != matrix_B[0] || matrix_A[1] != matrix_B[1]) {
        input_test(ERROR_INPUT);
        }
        break;
    }
}

void read_matrix(int *matrix) {
    int row = matrix[0];
    int column = matrix[1];

    for (int i = 0; i < row; i++) {
        for (int j = 0; j < column; j++) {
            printf("%d", matrix[i * column + j + 2]);
            if (j != column - 1) {
                printf(" ");
            }
        }
        printf("\n");
    }
}

void clear_matrix_memory(int *matrix) {
    for (int i = 0; i < matrix[0] * matrix[1]; i++) {
        matrix[i + 2] = 0;
    }
}

int *matrix_multiplication(int *matrix_A, int *matrix_B, int idx) {
    int *new_matrix = reallocation_matrix(matrix_A[0] * matrix_B[1]);

    new_matrix[0] = matrix_A[0];
    new_matrix[1] = matrix_B[1];

    for (int new_row = 0; new_row < matrix_A[0]; new_row++) {
        for (int new_column = 0; new_column < matrix_B[1]; new_column++) {
            for (int row = 0; row < matrix_B[0]; row++) {
                new_matrix[new_row * matrix_B[1] + new_column + 2] +=
                    matrix_A[new_row * matrix_A[1] + row + 2] *
                    matrix_B[row * matrix_B[1] + new_column + 2];
            }
        }
    }

    free(matrix_A);
    free(matrix_B);
    matrix_A = NULL;
    matrix_B = NULL;
    return new_matrix;
}

int *matrix_add(int *matrix_A, int *matrix_B, int idx) {
    int *new_matrix = reallocation_matrix(matrix_A[1] * matrix_B[0]);

    new_matrix[0] = matrix_A[0];
    new_matrix[1] = matrix_B[1];

    for (int i = 0; i < matrix_A[0]; i++) {
        for (int j = 0; j < matrix_A[1]; j++) {
            new_matrix[i * matrix_A[1] + j + 2] =
                matrix_A[i * matrix_A[1] + j + 2] +
                matrix_B[i * matrix_A[1] + j + 2];
        }
    }
    free(matrix_A);
    free(matrix_B);
    matrix_A = NULL;
    matrix_B = NULL;
    return new_matrix;
}

void adjust_matrix_array(int **matrix_array, int *size) {
    for (int i = 0; i < *size; i++) {
        if (matrix_array[i] == NULL) {
            matrix_array[i] = matrix_array[i + 1];
            matrix_array[i + 1] = NULL;
        }
    }
}

void adjust_operations(char *operations, int size) {
    for (int i = 0; i < size; i++) {
        if (operations[i] == '0') {
            operations[i] = operations[i + 1];
            operations[i + 1] = '0';
        }
    }
    operations[size] = '0';
}

int *matrix_calculation(int **matrix_array, char *operations,
                        int number_of_matrixes) {

    int matrix_array_size = number_of_matrixes - 1;
    int operations_size = number_of_matrixes - 2;

    for (int op_idx = operations_size; op_idx > -1; op_idx--) {
        // Reads through all the multiplication operations
        char operation = '0';
        operation = operations[op_idx];
        if (operation == MULTIPLICATION) {
            matrix_compatibility(matrix_array[op_idx],matrix_array[op_idx + 1],
                            MULTIPLICATION);

            matrix_array[op_idx] = matrix_multiplication(
            matrix_array[op_idx], matrix_array[op_idx + 1], op_idx);

            matrix_array[op_idx + 1] = NULL;
            operations[op_idx] = '0';

            adjust_matrix_array(*&matrix_array, &matrix_array_size);
            adjust_operations(*&operations, operations_size);

            matrix_array_size -= 1;
            operations_size -= 1;
        }
    }

    if (matrix_array_size == 0) {
        // Checks if all operations were done base on remaining matrixes

        return matrix_array[0];
    }

    for (int op_idx = operations_size; op_idx > -1; op_idx--) {
        // Reads through all the addition operations
        matrix_compatibility(matrix_array[op_idx], matrix_array[op_idx + 1], ADD);

        matrix_array[op_idx] =
            matrix_add(matrix_array[op_idx], matrix_array[op_idx + 1], op_idx);

        operations[op_idx] = '0';

        adjust_matrix_array(*&matrix_array, &matrix_array_size);
        adjust_operations(*&operations, operations_size);

        matrix_array_size -= 1;
        operations_size -= 1;
    }
    return matrix_array[0];
}
