#include "Item.h"

// Default constructor, initialises an unnamed item that is available
Item::Item() {
    name = "Unnamed Item";
    available = true;
}

// Constructor with name parameter, initialises an item with the given name that is available
Item::Item(std::string& name) {
    setName(name);
    available = true;
}

// Getter for item name
string Item::getName() const {
    return name;
}

// Setter for item name
void Item::setName(const string& name) {
    Item::name = name;
}

// Checks if the item is available
bool Item::checkAvailability() const {
    return available;
}

// Sets the availability of the item
void Item::setAvailability(const bool ave) {
    Item::available = ave;
}