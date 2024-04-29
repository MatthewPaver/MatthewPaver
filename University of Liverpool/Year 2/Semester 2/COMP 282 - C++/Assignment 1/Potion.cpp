#include "Potion.h"  // Include the Potion class definition

// Getter for the strength attribute
int Potion::getStrength() const {
    return strength;
}

// Setter for the strength attribute
void Potion::setStrength(int strength) {
    Potion::strength = strength;
}

// Default constructor
Potion::Potion() {
    strength = 0;
}

// Constructor with strength parameter
Potion::Potion(int strength) {
    setStrength(strength);  // Set the strength using the setter
}

// Constructor with name and strength parameters
Potion::Potion(string name, int strength) {
    setName(name);  // Set the name using the setName method from the Item base class
    setStrength(strength);  // Set the strength using the setter
}