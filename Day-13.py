#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, i;
    int *ptr;

    printf("Kitne elements chahiye? ");
    scanf("%d", &n);

    // memory allocate
    ptr = (int*) malloc(n * sizeof(int));

    if(ptr == NULL) {
        printf("Memory nahi mili!\n");
        return 0;
    }

    printf("%d numbers daalo:\n", n);
    for(i = 0; i < n; i++) {
        scanf("%d", &ptr[i]);
    }

    printf("Tumne ye daale:\n");
    for(i = 0; i < n; i++) {
        printf("%d ", ptr[i]);
    }

    free(ptr); // memory free
