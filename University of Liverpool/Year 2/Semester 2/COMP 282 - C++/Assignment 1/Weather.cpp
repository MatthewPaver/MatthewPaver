#include "Weather.h"
#include <cstdlib>  // For rand()

// Global variable to track game time
static int gameTime = 0;
Weather currentWeather = CLEAR; // Definition of currentWeather

void incrementTime() {
    gameTime++; // Increment game time each turn
}

bool isDay() {
    return gameTime % 24 < 12; // Daytime is from 0 to 11
}

void changeWeather() {
    currentWeather = static_cast<Weather>(rand() % 3); // Randomly change weather each turn
}

void applyWeatherEffects(Player &player) {
    switch (currentWeather) {
        case RAIN:
            player.movementSpeed *= 0.9; // Reduce movement speed in rain
            break;
        case FOG:
            player.accuracy *= 0.9; // Reduce accuracy in fog
            break;
        default:
            break; // No effect in clear weather
    }
}

void removeWeatherEffects(Player &player) {
    switch (currentWeather) {
        case RAIN:
            player.movementSpeed /= 0.9; // Restore movement speed after rain
            break;
        case FOG:
            player.accuracy /= 0.9; // Restore accuracy after fog
            break;
        default:
            break; // No effect to remove in clear weather
    }
}
