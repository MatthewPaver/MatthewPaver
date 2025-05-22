#ifndef ITEM_H
#define ITEM_H

#include <string>

using namespace std;

// Item class
class Item {
private:
    string name;       // Name of the item
    bool available;    // Availability status of the item

public:
    // Getter for item name
    string getName() const;
    // Setter for item name
    void setName(const string& name);

    // Checks if the item is available
    bool checkAvailability() const;
    // Sets the availability of the item
    void setAvailability(const bool ave);

    Item();            
    Item(string& name);// Constructor with name parameter
    virtual ~Item() {} // Virtual destructor
};

#endif //ITEM_H