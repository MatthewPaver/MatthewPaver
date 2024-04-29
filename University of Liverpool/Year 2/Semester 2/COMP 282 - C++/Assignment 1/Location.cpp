#include "Location.h"

// Default constructor, initialises all directions to null
Location::Location() {
    east = west = north = south = nullptr;
}

// Setter for location name
void Location::setName(string name) {
    this->name = name;
}

// Setter for location description
void Location::setDescription(string description) {
    this->description = description;
}

// Getter for location name
string Location::getName() {
    return name;
}

// Getter for location description
string Location::getDescription() {
    return description;
}

// Adds an exit in a specific direction to another location
void Location::addExit(Direction direction, Location* leadToLocation) {
    switch (direction) {
        case NORTH:
            north = leadToLocation;
            break;
        case SOUTH:
            south = leadToLocation;
            break;
        case EAST:
            east = leadToLocation;
            break;
        case WEST:
            west = leadToLocation;
            break;
    }
}

// Returns a map of exits and the locations they lead to
map<Direction, Location*> Location::getExits() {
    map<Direction, Location*> exitsMap;

    if (north != nullptr) {
        exitsMap.insert(pair<Direction, Location*>(NORTH, north));
    }
    if (south != nullptr) {
        exitsMap.insert(pair<Direction, Location*>(SOUTH, south));
    }
    if (east != nullptr) {
        exitsMap.insert(pair<Direction, Location*>(EAST, east));
    }
    if (west != nullptr) {
        exitsMap.insert(pair<Direction, Location*>(WEST, west));
    }

    return exitsMap;
}

// Adds a monster to the location
void Location::addMonster(Monster* monsterToSpawn) {
    monsters.push_back(monsterToSpawn);
}

// Deletes a monster from the location by setting its hit points to 0
void Location::delMonster(Monster* monsterToDel) {
    for (int i = 0; i < monsters.size(); i++) {
        if (monsters[i]->getName() == monsterToDel->getName()) {
            monsters[i]->setHitPoints(0);
            return;
        }
    }
}

// Returns a vector of monsters present at the location
vector<Monster*> Location::getMonsters() {
    return monsters;
}

// Adds an item to the location, item type is determined by dynamic casting
void Location::addItem(Item* itemToAdd) {
    if (dynamic_cast<Weapon*>(itemToAdd)) {
        weapons.push_back((dynamic_cast<Weapon*>(itemToAdd)));
    } else if (dynamic_cast<Potion*>(itemToAdd)) {
        potions.push_back((dynamic_cast<Potion*>(itemToAdd)));
    } else if (dynamic_cast<Treasure*>(itemToAdd)) {
        treasure.push_back((dynamic_cast<Treasure*>(itemToAdd)));
    } else if ((dynamic_cast<Armour*>(itemToAdd))){
        armours.push_back((dynamic_cast<Armour*>(itemToAdd)));
    }
}

// Prints all available items at the location
void Location::PrintAvailabeItem()
{
    int num = 0;
    cout << "Potions:\t";
    for (const auto& potion : potions) {
        if (potion->checkAvailability() == true)
        {
            cout << "- " << potion->getName() << " : " << potion->getStrength() << "\t";
            num++;
        }
    }
    if(num == 0)
    {
        cout << "None";
    }
    cout << endl;
    num = 0;

    cout << "Treasures:\t";
    for (const auto&treas  : treasure) {
        if (treas->checkAvailability() == true)
        {
            cout << "- " << treas->getName() << " : " << treas->getValue() << "\t";
            num++;
        }
    }
    if (num == 0)
    {
        cout << "None";
    }
    cout << endl;

    cout << "Weapons:\t";
    for (const auto& weapon : weapons) {
        if (weapon->checkAvailability() == true)
        {
            cout << "- " << weapon->getName() << " : " << weapon->getPower() << "\t";
            num++;
        }
    }
    if (num == 0)
    {
        cout << "None";
    }
    cout << endl;

    cout << "Armours:\t";
    for (const auto& armour : armours) {
        if (armour->checkAvailability() == true)
        {
            cout << "- " << armour->getName() << " : " << armour->getProtection() << "\t";
            num++;
        }
    }
    if (num == 0)
    {
        cout << "None";
    }
    cout << endl;
}

// Adds an item to a specific location, item type is determined by dynamic casting
void Location::addItem(Item* itemToAdd, Location* itemLocation) {
    if (dynamic_cast<Weapon*>(itemToAdd)) {
        weapons.push_back((dynamic_cast<Weapon*>(itemToAdd)));
    } else if (dynamic_cast<Potion*>(itemToAdd)) {
        potions.push_back((dynamic_cast<Potion*>(itemToAdd)));
    } else if (dynamic_cast<Treasure*>(itemToAdd)) {
        treasure.push_back((dynamic_cast<Treasure*>(itemToAdd)));
    }
}