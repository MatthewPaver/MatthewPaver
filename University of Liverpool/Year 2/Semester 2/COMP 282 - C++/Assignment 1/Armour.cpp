#include "Armour.h"
#include "Item.h"

// Constructor with parameters for name, description, and protection
Armour::Armour(string name, string description, int protection) {
    setName(name);               // Set the name of the armour
    setDescription(description); // Set the description of the armour
    setProtection(protection);   // Set the protection value of the armour
}

// Getter for armour description
string Armour::getDescription() {
    return description;   
}

// Setter for armour description
void Armour::setDescription(string description) {
    this->description = description;
}

// Getter for armour protection value
int Armour::getProtection() {
    return protection;         
}

// Setter for armour protection value
void Armour::setProtection(int protection) {
    this->protection = protection; 
}