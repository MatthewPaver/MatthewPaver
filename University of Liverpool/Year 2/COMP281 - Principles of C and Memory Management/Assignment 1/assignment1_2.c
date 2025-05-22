#include <stdio.h>

int main() {
    char inputChar;
    int letterCount = 0, digitCount = 0, spaceCount = 0, otherCount = 0; // Counters

    // Read characters until a newline or EOF
    while ((inputChar = getchar()) != EOF && inputChar != '\n') {
        // Check if character is a letter
        if ((inputChar >= 'a' && inputChar <= 'z') || (inputChar >= 'A' && inputChar <= 'Z')) {
            letterCount++;
        } 
        // Check if character is a digit
        else if (inputChar >= '0' && inputChar <= '9') {
            digitCount++;
        }
        // Check if character is a space
        else if (inputChar == ' ') {
            spaceCount++;
        } 
        // If none of the above, it's an other character
        else {
            otherCount++;
        }
    }

    // Output the counts
    printf("%d %d %d %d\n", letterCount, digitCount, spaceCount, otherCount);
    return 0;
}
