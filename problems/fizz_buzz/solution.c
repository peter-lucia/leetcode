#include <stdio.h>
#include <stdlib.h> //needed to use malloc

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
void digitToString(char *c, int i) {
    sprintf(c, "%d", i);
}

char** fizzBuzz(int n, int* returnSize) {

    char **blah = (char **)malloc(sizeof(char *)*n); //allocate n character pointers
    for (int i =0;i<n;i++ ) {
        blah[i] = (char *)malloc(sizeof(char) * 10); //allocate 10 characters for each string
    }
    for (int i=1;i<=n;i++) {
        if ( i % 3 == 0 && i % 5 == 0) {
            blah[i-1] = "FizzBuzz\0";
        }
        else if (i % 3 == 0) {
            blah[i-1] = "Fizz\0";
        }
        else if (i % 5 == 0) {
            blah[i-1] = "Buzz\0";
        }
        else {
            digitToString(blah[i-1], i);
        }
    }
    *returnSize = n;
    return blah;
}