#include "Weapon.h"  // Include the Weapon class definition

// Getter for the power attribute
int Weapon::getPower() const {
    return power;
}

// Setter for the power attribute
void Weapon::setPower(int power) {
    Weapon::power = power;
}

// Default constructor
Weapon::Weapon() {
    power = 0;
}

// Constructor with power parameter
Weapon::Weapon(int power) {
    setPower(power);
}

// Constructor with name and power parameters
Weapon::Weapon(string name, int power) {
    setName(name);
    setPower(power); 
}