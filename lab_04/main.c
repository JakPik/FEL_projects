#include <stdio.h>

#define ERROR_INPUT 100
#define ERROR_LIMIT 101

#define MIN_VALUE 1
#define MAX_VALUE 10

int main(int argc, char **argv) {
    int ret = 0;

    int n;
    if (scanf("%d", &n) != 1) {
        fprintf(stderr, "ERROR: Cannot read integer value from the standard input\n");
        ret = ERROR_INPUT;
    } else if (n < MIN_VALUE || n > MAX_VALUE) {
        fprintf(stderr, "ERROR: Given value %d is not within the range [%d, %d]\n", n, MIN_VALUE, MAX_VALUE);
        ret = ERROR_LIMIT;
    } else {
        for (int i = n; i > 0; --i) {
            for (int j = 0; j < i; ++j) {
                putchar('*');
            }
            putchar('\n');
        }
    }

    return ret;
}
