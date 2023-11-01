#include <stdio.h>

int main() {
    int a = 7;
    int *ptr_1 = &a;
    int b = *ptr_1;
    int *ptr_2 = &b;
    printf("     a: %d\n", a);
    printf(" ptr_1: %p\n", ptr_1);
    printf("*ptr_1: %d\n", *ptr_1);
    printf("     b: %d\n", b);
    printf(" ptr_2: %p\n", ptr_2);
    printf("*ptr_2: %d\n", *ptr_2);
    printf("----------------------------------\n");

    b = 8;
    printf("    a: %d\n", a);
    printf(" ptr_1: %p\n", ptr_1);
    printf("*ptr_1: %d\n", *ptr_1);
    printf("    b: %d\n", b);
    printf(" ptr_2: %p\n", ptr_2);
    printf("*ptr_2: %d\n", *ptr_2);
    printf("----------------------------------\n");

    ptr_1 = ptr_2;
    printf("     a: %d\n", a);
    printf(" ptr_1: %p\n", ptr_1);
    printf("*ptr_1: %d\n", *ptr_1);
    printf("     b: %d\n", b);
    printf(" ptr_2: %p\n", ptr_2);
    printf("*ptr_2: %d\n", *ptr_2);
    printf("----------------------------------\n");

    *ptr_1 = 9;
    printf("     a: %d\n", a);
    printf(" ptr_1: %p\n", ptr_1);
    printf("*ptr_1: %d\n", *ptr_1);
    printf("     b: %d\n", b);
    printf(" ptr_2: %p\n", ptr_2);
    printf("*ptr_2: %d\n", *ptr_2);
    printf("----------------------------------\n");
    
    return 0;
}
