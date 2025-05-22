#ifndef PLAYER_H
#define PLAYER_H

#include "Character.h"  // Include the base class Character header
#include "Location.h"   // Include Location class for player's location
#include "Weapon.h"     // Include Weapon class for player's weapons
#include "Potion.h"     // Include Potion class for player's potions
#include "Treasure.h"   // Include Treasure class for player's treasures

#include <vector>       // For using the std::vector container

using namespace std;   // Use standard namespace identifiers without the std:: prefix

// Player class, inherits from Character
class Player : public Character {
private:
    int score;                  // Player's score
    Location currentLocation;   // Player's current location

public:
    Player();                   
    vector<Weapon> weapons;     // Vector of player's weapons
    vector<Potion> potions;     // Vector of player's potions
    vector<Treasure> treasures; // Vector of player's treasures

    int getScore();             // Getter for score
    void setScore(int score);   // Setter for score
    Location getCurrentLocation();  // Getter for current location
    void setCurrentLocation(Location currentLocation);  // Setter for current location
    void applyWeatherEffects(); // Applies weather effects
    void removeWeatherEffects(); // Removes weather effects

    bool combat(Monster monster);  // Handles combat with a monster
    Weapon getMostPowerfulWeapon();  // Retrieves the most powerful weapon

    double movementSpeed = 1.0;  // Default speed
    double accuracy = 1.0;       // Default accuracy
};

#endif // PLAYER_H