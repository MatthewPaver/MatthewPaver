#include <stdio.h>

int main() {
    int numerator, denominator, n;
    scanf("%d %d %d", &numerator, &denominator, &n); // Read inputs

    numerator %= denominator; // Get the initial remainder

    // Loop to find the n-th digit after the decimal point
    for (int i = 0; i < n; i++) {
        numerator *= 10; // Increase the precision
        int digit = numerator / denominator; // Get the current digit

        if (i == n - 1) {
            printf("%d\n", digit); // Print the n-th digit
        }

        numerator %= denominator; // Update the remainder
    }

    return 0;
}
