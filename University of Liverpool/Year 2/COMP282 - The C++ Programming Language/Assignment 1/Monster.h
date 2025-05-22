#ifndef MONSTER_H
#define MONSTER_H

#include "Character.h"  // Include the base class Character header
#include "Item.h"       // Include the Item class for monster's loot
#include <vector>       // For using the std::vector container

using namespace std;    // Use standard namespace identifiers without the std:: prefix

// Monster class, inherits from Character
class Monster : public Character {
private:
    vector<Item*> loot;  // Vector of pointers to items, representing the monster's loot

public:
    Monster(string name, int hitPoints);  // Constructor with name and hitPoints parameters

    vector<Item*> getLoot();  // Getter for the loot vector

    void setLoot(Item *item);  // Adds an item to the monster's loot
};

#endif // MONSTER_H