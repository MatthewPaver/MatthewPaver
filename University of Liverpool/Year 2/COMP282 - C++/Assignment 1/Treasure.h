#ifndef TREASURE_H
#define TREASURE_H

#include "Item.h"  // Include the base class Item header

// Treasure class, inherits from the Item class
class Treasure : public Item{
private:
    int value;  // Monetary value of the treasure

public:
    int getValue() const;  // Getter for the value attribute

    void setValue(int value);  // Setter for the value attribute

    Treasure(); 

    Treasure(string name, int value);  // Constructor with name and value parameters

    virtual ~Treasure() {}  // Virtual destructor for proper cleanup of derived class objects
};

#endif // TREASURE_H