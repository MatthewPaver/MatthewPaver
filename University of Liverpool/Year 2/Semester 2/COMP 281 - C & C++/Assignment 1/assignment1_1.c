#include <stdio.h>

int main() {
    int startRadius, endRadius;
    scanf("%d %d", &startRadius, &endRadius); // Reading the start and end radii

    float areaSum = 0.0, circumferenceSum = 0.0; // Initialise sums
    const float PI = 3.14; // Constant value for Pi

    // Loop through each radius from start to end
    for (int radius = startRadius; radius <= endRadius; ++radius) {
        float area = PI * radius * radius; // Calculate area for current radius
        float circumference = 2 * PI * radius; // Calculate circumference for current radius

        // Add current area and circumference to their respective sums
        areaSum += area;
        circumferenceSum += circumference;
    }

    // Print the total sum of areas and circumferences, each on a new line
    printf("%.3f\n", areaSum); // Print sum of areas with three decimal places
    printf("%.3f\n", circumferenceSum); // Print sum of circumferences with three decimal places
    return 0;
}
