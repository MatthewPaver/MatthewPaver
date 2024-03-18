#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void compressLine(const char *line) { // Compress a line using run-length encoding
    int count = 1;
    char current = line[0];

    for (int i = 1; i <= strlen(line); i++) {
        if (line[i] == current && count < 255) {
            count++;
        } else {
            if (count >= 3) {
                printf("%c%c%c%02X", current, current, current, count);
            } else {
                for (int j = 0; j < count; j++) {
                    printf("%c", current);
                }
            }
            current = line[i];
            count = 1;
        }
    }
    printf("\n");
}

void expandLine(const char *line) { // Expand a line using run-length encoding
    for (int i = 0; i < strlen(line);) {
        if (i < strlen(line) - 3 && line[i] == line[i + 1] && line[i + 1] == line[i + 2]) {
            int count = (strtol(&line[i + 3], NULL, 16) & 0xFF);
            for (int j = 0; j < count; j++) {
                printf("%c", line[i]);
            }
            i += 5; // Move past the encoded part
        } else {
            printf("%c", line[i]);
            i++;
        }
    }
    printf("\n");
}

int main() {
    char mode;
    char line[133]; // Including space for null terminator

    // Read mode from the first line
    scanf("%c%*c", &mode); // The %*c consumes the newline character after the mode character

    while (fgets(line, sizeof(line), stdin)) { // Read lines until EOF
        line[strcspn(line, "\n")] = 0; // Remove trailing newline

        if (mode == 'C') {
            compressLine(line);
        } else if (mode == 'E') {
            expandLine(line);
        }
    }

    return 0;
}
