#ifndef CHARACTER_H
#define CHARACTER_H

#include <iostream>
#include <string>
#include <vector>
#include "Armour.h"

using namespace std;

// Character class
class Character {
protected:
    string name;                // Name of the character
    int hitPoints;              // Hit points of the character
    vector<Armour> armour;      // Vector of Armour objects representing the character's armour

public:
    Character();                

    // Setter for character name
    void setName(const string& name);
    // Getter for character name
    string getName() const;

    // Getter for character hit points
    int getHitPoints() const;
    // Setter for character hit points
    void setHitPoints(int hitPoints);
    // Method to apply damage to the character, reducing hit points
    void takeHit(int damage);

    // Method to add an Armour object to the character's armour vector
    void addArmour(Armour armour);
    // Getter for the character's armour vector
    vector<Armour> getArmour();
    // Setter for the character's armour vector
    void setArmour(vector<Armour> armour);
};

#endif //CHARACTER_H