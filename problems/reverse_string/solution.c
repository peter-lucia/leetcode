char* reverseString(char *s) {
    if (s == NULL) {
        return NULL;
    }
    if (s == "") {
        return s;
    }
    int length = strlen(s);
    char *result = malloc(sizeof(char)*length*2);
    for (int i=0;i<length;i++) {

      //  char temp = s[length-i-1];
        result[i] = s[length-i-1];
    }
    result[length] = '\0';
    return result;
}