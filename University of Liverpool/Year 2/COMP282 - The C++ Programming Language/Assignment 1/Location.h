#ifndef LOCATION_H
#define LOCATION_H

#include <string>  
#include <map>     
#include "Direction.cpp"
#include "Monster.h"  
#include "Item.h"     
#include "Weapon.h"   
#include "Potion.h"   
#include "Treasure.h" 
#include "Armour.h"   

using namespace std;  

// Location class
class Location {
private:
    string name;       // Name of the location
    string description;// Description of the location

    // Pointers to adjacent locations
    Location* north;   
    Location* south;
    Location* east;
    Location* west;

    vector<Monster*> monsters;  // Monsters present at the location

public:
    // Items of various types at the location
    vector<Weapon*> weapons;
    vector<Potion*> potions;
    vector<Treasure*> treasure;
    vector<Armour*> armours;

    Location();

    // Getter and setter for the name of the location
    string getName();
    void setName(string name);

    // Getter and setter for the description of the location
    string getDescription();
    void setDescription(string description);

    // Adds an exit to the location in a specific direction leading to another location
    void addExit(Direction direction, Location* leadToLocation);
    // Returns a map of exits showing which locations they lead to
    map<Direction, Location*> getExits();

    // Adds a monster to the location
    void addMonster(Monster* monsterToSpawn);
    // Deletes a monster from the location
    void delMonster(Monster* monsterToDel);
    // Returns a vector of monsters present at the location
    vector<Monster*> getMonsters();

    // Adds an item to the location
    void addItem(Item* itemToAdd);
    // Print all available items at the location
    void PrintAvailabeItem();
    // Virtual method to add an item to a specific location
    virtual void addItem(Item* itemToAdd, Location* itemLocation);
};

#endif // LOCATION_H