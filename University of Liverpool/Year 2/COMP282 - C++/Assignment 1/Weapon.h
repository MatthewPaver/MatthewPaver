#ifndef WEAPON_H
#define WEAPON_H

#include <string> // For using the std::string type
#include "Item.h" // Include the base class Item header

using namespace std; // avoid collisions with identically named functions in other libraries

// Weapon class, inherits from the Item class
class Weapon : public Item{
private:
    int power; // Power of the weapon

public:
    int getPower() const; // Getter for the power attribute

    void setPower(int power); // Setter for the power attribute

    Weapon();

    Weapon(int power); // Constructor with power parameter

    Weapon(string name, int power); // Constructor with name and power parameters
};

#endif // WEAPON_H