#ifndef ARMOUR_H
#define ARMOUR_H

#include <string>
#include "Item.h"

using namespace std;

// Armour class, derived from Item class
class Armour : public Item{
private:
    string description;  // Description of the armour
    int protection;      // Protection value of the armour

public:
    // Constructor with parameters for name, description, and protection
    Armour(string name, string description, int protection);

    // Getter for armour description
    string getDescription();
    // Setter for armour description
    void setDescription(string description);

    // Getter for armour protection value
    int getProtection();
    // Setter for armour protection value
    void setProtection(int protection);
};

#endif //ARMOUR_H