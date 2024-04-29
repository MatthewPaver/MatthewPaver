#ifndef WEATHER_H
#define WEATHER_H

#include "Player.h"

enum Weather { CLEAR, RAIN, FOG };

extern Weather currentWeather; // Declaration of currentWeather

void incrementTime(); // Function to increment game time
bool isDay(); // Function to check if it is day
void changeWeather(); // Function to change the weather
void applyWeatherEffects(Player &player); // Function to apply weather effects
void removeWeatherEffects(Player &player); // Function to remove weather effects

#endif
