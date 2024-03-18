#include <stdio.h>

// Custom absolute value function
int custom_abs(int value) {
    return (value < 0) ? -value : value;
}

int main() {
    int numbers[10]; // Array to hold the input numbers

    // Read the 10 integers
    for (int i = 0; i < 10; i++) {
        scanf("%d", &numbers[i]);
    }

    int minIndex = 0; // Index of the minimum absolute value
    // Loop to find the index of the minimum absolute value using custom_abs
    for (int i = 1; i < 10; i++) {
        if (custom_abs(numbers[i]) < custom_abs(numbers[minIndex])) {
            minIndex = i;
        }
    }

    // Swap the minimum absolute value with the last element
    int temp = numbers[minIndex];
    numbers[minIndex] = numbers[9];
    numbers[9] = temp;

    // Print the array after the swap
    for (int i = 0; i < 10; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");

    return 0;
}
