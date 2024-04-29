#ifndef POTION_H
#define POTION_H

#include "Item.h"  // Include the base class Item header

// Potion class, inherits from the Item class
class Potion : public Item{
private:
    int strength;  // Strength of the potion

public:
    int getStrength() const;  // Getter for the strength attribute

    void setStrength(int strength);  // Setter for the strength attribute

    Potion();

    Potion(int strength);  // Constructor with strength parameter

    Potion(string name, int strength);  // Constructor with name and strength parameters
};

#endif // POTION_H