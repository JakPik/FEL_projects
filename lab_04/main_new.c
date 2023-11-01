#include <stdio.h>

#define ERROR_INPUT 100
#define ERROR_LIMIT 101

#ifndef MIN_VALUE
#define MIN_VALUE 1
#endif

#ifndef MAX_VALUE
#define MAX_VALUE 10
#endif

int read_input(int *m);
void print_error_msg(int ret, int n);
void print_line(int size);
void print_triangle(int size);

int main(int argc, char **argv) {
    int ret = 0;

    int n;
    ret = read_input(&n);
    if (ret == 0) {
        print_triangle(n);
    }
    print_error_msg(ret, n);

    return ret;
}

int read_input(int *m) {
    int ret = 0;
    if (scanf("%d", m) != 1) {
        ret = ERROR_INPUT;
    } else if (*m < MIN_VALUE || *m > MAX_VALUE) {
        ret = ERROR_LIMIT;
    }
    return ret;
}

void print_error_msg(int ret, int n) {
    switch (ret) {
        case ERROR_INPUT:
            fprintf(stderr, "ERROR: Cannot read integer value from the standard input\n");
            break;
        case ERROR_LIMIT:
            fprintf(stderr, "ERROR: Given value %d is not within the range [%d, %d]\n", n, MIN_VALUE, MAX_VALUE);
            break;
    }
}

void print_line(int length) {
    for (int j = 0; j < length; ++j) {
        putchar('*');
    }
    putchar('\n');
}

void print_triangle(int size) {
    for (int i = size; i > 0; --i) {
        print_line(i);
    }
}