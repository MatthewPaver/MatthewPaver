#include "Character.h"

// Default constructor, initialises character with 0 hit points
Character::Character() {
    hitPoints = 0;
}

// Setter for character
void Character::setName(const string& name) {
    this->name = name;
}

// Getter for character
string Character::getName() const {
    return name;
}

// Setter for character hit points
void Character::setHitPoints(int hitPoints) {
    this->hitPoints = hitPoints;
}

// Getter for character hit points
int Character::getHitPoints() const {
    return hitPoints;
}

// Method to apply damage to the character, reducing hit points
void Character::takeHit(int damage) {
    setHitPoints(getHitPoints() - damage);
}

// Method to add an Armour object to the character's armour vector
void Character::addArmour(Armour armour) {
    this->armour.push_back(armour);
}

// Getter for the character's armour vector
vector<Armour> Character::getArmour() {
    return armour;
}

// Setter for the character's armour vector
void Character::setArmour(vector<Armour> armour) {
    this->armour = armour;
}