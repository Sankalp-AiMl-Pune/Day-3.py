#include <stdio.h>
#include <string.h>

int main() {
    char text[100];
    int key = 3, i;

    printf("Text daalo encrypt karne ke liye: ");
    gets(text); // ya fgets use kar sakta hai

    for(i = 0; i < strlen(text); i++) {
        text[i] = text[i] + key; // har letter ko 3 se aage badha do
    }

    printf("Encrypted Text: %s\n", text);

    // Decrypt karke wapas
    for(i = 0; i < strlen(text); i++) {
        text[i] = text[i] - key;
    }
    printf("Decrypted Text: %s\n", text);

    return 0;
}
