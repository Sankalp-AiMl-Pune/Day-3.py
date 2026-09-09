#include <stdio.h>

int main() {
    FILE *fptr;
    char text[100];

    // 1. File me likhna
    fptr = fopen("hacklog.txt", "w");
    fprintf(fptr, "User: admin\nLogin: Success\n");
    fclose(fptr);

    // 2. File ko padhna
    fptr = fopen("hacklog.txt", "
