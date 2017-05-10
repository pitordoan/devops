#include <stdio.h>
#include <string.h>

int main() {
    char s[] = "Hello world";

    int len = strlen(s);
    char result[len];

    int j = len - 1;
    for (int i=0; i<len; i++) {
        result[i] = s[j--];
    }

    printf("Reverse of %s is %s\n", s, result);
}