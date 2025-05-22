#include "Monster.h"  // Include the Monster class definition

// Constructor for Monster, initialises a monster with a name and hit points
Monster::Monster(string name, int hitPoints) {
    this->name = name;            // Set the monster's name
    this->hitPoints = hitPoints;  // Set the monster's hit points
}

// Getter for the loot vector containing pointers to the items a monster can drop
vector<Item *> Monster::getLoot() {
    return loot;  // Return the vector containing the loot items
}

// Method to add an item to the monster's loot
void Monster::setLoot(Item *item) {
    loot.push_back(item);  // Add the item pointer to the loot vector
}