#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char pass[100];
    int hasUpper=0, hasLower=0, hasDigit=0, hasSpecial=0, i;

    printf("Apna password daalo: ");
    scanf("%s", pass);

    if(strlen(pass) < 8) {
        printf("Weak: Password 8 se bada hona chahiye\n");
        return 0;
    }

    for(i=0; i<strlen(pass); i++) {
        if(isupper(pass[i])) hasUpper=1;
        else if(islower(pass[i])) hasLower=1;
        else if(isdigit(pass[i])) hasDigit=1;
        else hasSpecial=1;
    }

    if(hasUpper && hasLower && hasDigit && hasSpecial) {
        printf("Strong Password! Good for Cyber Security\n");
    } else {
        printf("Medium Password: Upper, Lower, Number aur Symbol sab daalo\n");
    }

    return 0;
}
