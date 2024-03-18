#include <stdio.h>

#define MAX_SIZE 200 // Define maximum size of the string

int main() {
    char str[MAX_SIZE], temp; // String buffer and temporary variable for swapping
    fgets(str, MAX_SIZE, stdin); // Read the string including spaces

    int length = 0; // Find the length of the string
    while (str[length] != '\n' && str[length] != '\0') length++;

    // Swap characters starting from both ends of the string
    for (int i = 0; i < length / 2; i++) {
        temp = str[i];
        str[i] = str[length - 1 - i];
        str[length - 1 - i] = temp;
    }

    str[length] = '\0'; // Ensure the last character is null-terminated
    printf("%s", str); // Print the reversed string
    return 0;
}
