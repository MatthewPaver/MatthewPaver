#include "Player.h"
#include <ctime>  // For time-based random number generation

// Default constructor for Player, initialises score to 0
Player::Player() {
    score = 0;  // Initialise player score to zero at start
}

// Getter for the player's score
int Player::getScore() {
    return score;  // Return the current score of the player
}

// Setter for the player's score
void Player::setScore(int score) {
    this->score = score;  // Set the player's score to the provided value
}

// Getter for the player's current location
Location Player::getCurrentLocation() {
    return currentLocation;  // Return the current location of the player
}

// Setter for the player's current location
void Player::setCurrentLocation(Location currentLocation) {
    this->currentLocation = currentLocation;  // Set the current location to the provided location
}

// Function to simulate rolling a die, returning a random number between 1 and 6
int rollDice() {
    srand(time(nullptr));  // Seed the random number generator
    return (int)(rand() % 6 + 1);  // Return a random number from 1 to 6
}

// Function to calculate the total protection from equipped armour
int calculateProtection(vector<Armour> armour) {
    srand(time(nullptr));  // Seed the random number generator again

    int protection = 0;

    for (int i = 0; i < armour.size(); i++) {
        protection += armour[i].getProtection();  // Sum up the protection values of all armour pieces
    }

    // Return a random number between 0 and the total protection
    if (protection > 0)
        return (int)(rand() % protection + 1);
    return 0;
}

// Function to handle combat with a monster
bool Player::combat(Monster monster) {
    int newScore = monster.getHitPoints();
    while (true) {
        // Monster strikes first
        int monsterDamage = rollDice() * 2;  // Monster's damage is double the dice roll
        cout << "Monster inflicts " << monsterDamage << " damage." << endl;

        takeHit(monsterDamage - calculateProtection(armour));  // Apply damage to player, adjusted for armour
        // Check if player is defeated
        if (getHitPoints() <= 0) {
            cout << "Player is defeated!" << endl;
            return true;  // Return true if player is defeated
        }
        
        // Player strikes back
        int playerDamage = rollDice() + getMostPowerfulWeapon().getPower();  // Player's damage is dice roll plus weapon power
        cout << "Player inflicts " << playerDamage << " damage." << endl;
        monster.takeHit(playerDamage);  // Apply damage to monster

        // Display updated hitpoints
        cout << "Player hitpoints: " << getHitPoints() << endl;
        cout << "Monster hitpoints: " << monster.getHitPoints() << endl;

        // Check if monster is defeated
        if (monster.getHitPoints() <= 0) {
            setScore(getScore() + 10);  // Increase player's score
            cout << "Monster defeated! Score updated." << endl;
            return false;  // Return false, indicating monster defeated
        }
    }
}

// Function to get the most powerful weapon from player's arsenal
Weapon Player::getMostPowerfulWeapon() {
    Weapon mostPowerful = weapons[0];  // Start with the first weapon as the most powerful
    for (size_t i = 1; i < weapons.size(); i++) {
        if (weapons[i].getPower() > mostPowerful.getPower()) {
            mostPowerful = weapons[i];  // Update if a more powerful weapon is found
        }
    }
    return mostPowerful;  // Return the most powerful weapon
}