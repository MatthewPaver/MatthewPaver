#include "Treasure.h"  // Include the Treasure class definition

// Getter for the value attribute
int Treasure::getValue() const {
    return value;
}

// Setter for the value attribute
void Treasure::setValue(int value) {
    Treasure::value = value;
}

Treasure::Treasure() {
    value = 0;
}

// Constructor with name and value parameters
Treasure::Treasure(string name, int value) {
    setName(name);  // Set the name using the setName method from the Item base class
    setValue(value);  // Set the value using the setValue method
}