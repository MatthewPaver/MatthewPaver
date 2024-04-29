#include "Location.h"
#include "Player.h"
#include "Item.h"
#include "Weapon.h"
#include "Potion.h"
#include "Treasure.h"
#include "Weather.h"

// Initialise Location objects
Location cave; 
Location temple;
Location dungeon;
Location castle;
Location clearing;
Location hall;
Location garden;
Location library;
Location forest;
Location house;
Location ruins;
Location field;

// Initialise Treasure objects
Treasure emerald("Emerald", 40);
Treasure sapphire("Sapphire", 40);
Treasure diamond("Diamond", 60);
Treasure goldRing("Gold Ring", 60);
Treasure treasureChest("Treasure Chest", 200);
Treasure bagOfCoins("Bag of Coins", 50);
Treasure ruby("Ruby", 10);
Treasure cup("Cup", 20);
Treasure pearl("Pearl", 30);
Treasure key("Key", 5);
Treasure book("Book", 15);

// Initialise Weapon objects
Weapon dagger("Dagger", 5);
Weapon sword("Sword", 6);
Weapon stick("Stick", 1);
Weapon club("Club", 3);
Weapon crossbow("Crossbow", 10);

// Initialise Potion objects
Potion redHealing("Red Healing Potion", 40);
Potion purpleHealing("Purple Healing Potion", 30);
Potion blueHealing("Blue Healing Potion", 20);
Potion greenHealing("Green Healing Potion", 10);

// Initialise Armour objects
// ringmail, chainmail, shield, breastplate, helmet, gauntlet
// name, description, defence
Armour ringmail("Ringmail",
                "Ringmail Armour",
                5);
Armour chainmail("Chainmail",
                 "Chainmail Armour",
                 2);
Armour shield("Shield",
              "Shield Armour",
              3);
Armour breastplate("Breastplate",
                   "Breastplate Armour",
                   4);
Armour helmet("Helmet",
              "Helmet Armour",
              1);
Armour gauntlet("Gauntlet",
                "Gauntlet Armour",
                2);

// initialise Monster objects
Monster goblin = Monster("Goblin", 10);
Monster zombie = Monster("Zombie", 8);
Monster banshee = Monster("Banshee", 7);
Monster vampire = Monster("Vampire", 9);
Monster dragon = Monster("Dragon", 15);
Monster orc = Monster("Orc", 12);
Monster spectre = Monster("Spectre", 5);
Monster ghoul = Monster("Ghoul", 10);

Player player;
Player boss;

// Map to store the available exits from the player's current location
map<Direction, Location*> AvaliableExits;
bool gameRunning = true;


enum Command{
    MOVE_NORTH,
    MOVE_SOUTH,
    MOVE_EAST,
    MOVE_WEST,
    COLLECT,
    DRINK,
    INVENTORY,
    FIGHT,
    STATUS,
    QUIT,
    INVALID
};

void InitLocations(); // Initialise the locations in the game
void CreateMap(); // Create the map of locations

void InitPlayer(); // Initialise the player
void InitBoss(); // Initialise the boss

void DisplayPlayerLocation(); // Display the player's current location


string DirectionToString(Direction dir); // Convert a direction to a string
Direction StringToDirection(string dir); // Convert a string to a direction

Command StringToCommand(string command); // Convert a string to a command
void ProcessCommand(Command command); // Process the player's command

void TryMove(Direction direction); // Move the player in a specified direction
void CollectItems(); // Collect items from the player's current location
void ShowInventory(); // Show the player's inventory
void ShowPlayerStatus(); // Show the player's status
void DrinkPotion(); // Drink a potion

Monster SelectMonsterToFight();

int main()
{
    InitLocations(); // Initialise the locations in the game
    CreateMap(); // Create the map of locations

    InitPlayer(); // Initialise the player
    InitBoss(); // Initialise the boss

    std::cout << "Welcome to the Adventure Game! The aim is to defeat the Boss, but you score points for defeating monsters along the way. \n" << std::endl;
    std::cout << "You can use the following commands:" << std::endl;
    std::cout << "n, s, e, w - to move around the map" << std::endl;
    std::cout << "inventory - to check your inventory" << std::endl;
    std::cout << "status - Check your HP & Score" << std::endl;
    std::cout << "drink - drink any potions" << std::endl;
    std::cout << "collect - gather any items in your current location" << std::endl;
    std::cout << "fight - battle any monster in your current location" << std::endl;
    std::cout << "quit - exit the game \n" << std::endl;
    std::cout << "Remember, your choices and actions will determine your fate. Good luck!" << std::endl;
    std::cout << "-------------------------------------------------------------------" << std::endl;

    // Game Loop
    while (gameRunning) {
        // Increment time and change weather at the start of each turn
        incrementTime(); // Increment the game time each turn
        changeWeather(); // Change the weather each turn
        applyWeatherEffects(player); // Apply the effects of the current weather

        // Display the effect of current weather and time of day
        std::cout << "It is currently " << (isDay() ? "day." : "night.") << std::endl;
        std::string weatherDescription = (currentWeather == CLEAR ? "clear" : currentWeather == RAIN ? "raining" : "foggy");
        std::cout << "The weather is " << weatherDescription << ".\n"; 
        std::cout << "-------------------------------------------------------------------\n" << std::endl;

        DisplayPlayerLocation();

        std::string input = "";
        std::cout << "Enter a command: ";
        std::cin >> input;

        Command command = StringToCommand(input);
        ProcessCommand(command);

        // Remove weather effects at the end of the turn to reset for next cycle
        removeWeatherEffects(player);
    }

    return 0;
}

// Function to display the player's score and hit points
void DisplayScore() {
    cout << "Score: " << player.getScore() << endl;
    cout << "HitPoints: " << player.getHitPoints() << endl;
}
// Function to convert a direction to a string
string DirectionToString(Direction dir){
    switch(dir){
        case NORTH:
            return "North";
        case SOUTH:
            return "South";
        case EAST:
            return "East";
        case WEST:
            return "West";
    }
    return "";
}
// Function to convert a string to a direction
Direction StringToDirection(string dir){
    // dir = North, n, N
    if(dir == "North" || dir == "north" || dir == "n" || dir == "N"){
        return NORTH;
    }
    // dir = South, s, S
    if(dir == "South" || dir == "south" || dir == "s" || dir == "S"){
        return SOUTH;
    }
    // dir = East, e, E
    if(dir == "East" || dir == "east" || dir == "e" || dir == "E"){
        return EAST;
    }
    // dir = West, w, W
    if(dir == "West" || dir == "west" || dir == "w" || dir == "W"){
        return WEST;
    }
    return WEST;
}

// Function to convert a string to a command
Command StringToCommand(string command){
    if(command == "North" || command == "north" || command == "n" || command == "N"){
        return MOVE_NORTH;
    }
    if(command == "South" || command == "south" || command == "s" || command == "S"){
        return MOVE_SOUTH;
    }
    if(command == "East" || command == "east" || command == "e" || command == "E"){
        return MOVE_EAST;
    }
    if(command == "West" || command == "west" || command == "w" || command == "W"){
        return MOVE_WEST;
    }
    if(command == "collect"){
        return COLLECT;
    }
    if(command == "drink"){
        return DRINK;
    }
    if(command == "inventory" || command == "inv" ){
        return INVENTORY;
    }
    if(command == "fight"){
        return FIGHT;
    }
    if(command == "status"){
        return STATUS;
    }
    if(command == "quit" ){
        return QUIT;
    }

    return INVALID;
}
// Function to process the player's command
void ProcessCommand(Command command){
    switch(command){
        case MOVE_NORTH:
            TryMove(NORTH);
            break;
        case MOVE_SOUTH:
            TryMove(SOUTH);
            break;
        case MOVE_EAST:
            TryMove(EAST);
            break;
        case MOVE_WEST:
            TryMove(WEST);
            break;
        case COLLECT:
            CollectItems();
            break;
        case DRINK:
            DrinkPotion();
            break;
        case INVENTORY:
            ShowInventory();
            break;
    case FIGHT:
        if (!player.getCurrentLocation().getMonsters().empty()) { // Check if there are monsters in the location
            if (player.combat(SelectMonsterToFight())) {
                cout << "Game Over!" << endl;
                cout << "Player defeated! Score: " << player.getScore() << endl;
                cout << "HitPonits: " << player.getHitPoints() << endl; 

                gameRunning = false; // End the game
            }
        }
        else if (player.getCurrentLocation().getName() == "Cave") // Boss fight
        {
            cout << endl << endl;
            if (player.getHitPoints() > boss.getHitPoints())
            {
                cout << "Player is in cave... Player has HitPoints more than Boss" << endl;
                cout << "Congratulations! You have defeated the boss!" << endl;
                cout << "Your final score is: " << player.getScore() << endl;
                gameRunning = false;
            }
            else
            {
                cout << "Player is in cave... Boss has HitPoints more than Player" << endl;
                cout << "Player defeated! Score: " << player.getScore() << endl;
                gameRunning = false;
            }
        }
    else {
        cout << "There are no monsters to fight in this location." << endl;
    }
    break;


        case STATUS:
            ShowPlayerStatus();
            break;
        case QUIT:
            gameRunning = false;
            DisplayScore();
            cout << "Exiting game..." << endl;
            break;
        case INVALID:
            cout << "Unknown input, please try again." << endl;
            cout << "-------------------------------------------------------------------\n" << endl;
            break;
        default:
            cout << "Invalid command. Please enter a valid command." << endl;
            cout << "-------------------------------------------------------------------\n" << endl;
            break;
    }
}

// Function to display the current location of the player
void DisplayPlayerLocation(){
    // Print the name and description of the player's current location
    cout << "You are currently in the " << player.getCurrentLocation().getName() << ". " << player.getCurrentLocation().getDescription() << endl;
    
    // Print the available exits from the player's current location
    cout << "Your available exits are: " << endl;
    for(const auto& exit : AvaliableExits){
        Location* location = exit.second;
        // Print the name of the location and the direction to it
        cout << location->getName() << " (" << DirectionToString(exit.first) << ") " << endl;
    }

    // Display the player's current score
    DisplayScore();

    // Print the items available in the player's current location
    cout << "Items available in " << player.getCurrentLocation().getName() << endl;
    player.getCurrentLocation().PrintAvailabeItem();

    // Print the monsters in the player's current location
    cout << "Monsters in " << player.getCurrentLocation().getName() << endl;
    // Get the list of monsters in the current location
    auto monsters = player.getCurrentLocation().getMonsters();

    // Check if the list is empty
    if (monsters.empty()) {
        cout << "None" << endl;
    } else {
        // If not, loop through the list and print the monsters with more than 0 hit points
        for (Monster* monster : monsters) {
            if (monster->getHitPoints() > 0) {
                cout << "- " << monster->getName() << ": HP " << monster->getHitPoints() << endl;
            }
        }
    }

    cout << endl;
}

// Function to initialise the locations in the game
void InitLocations(){
    cave.setName("Cave");
    temple.setName("Temple");
    dungeon.setName("Dungeon");
    castle.setName("Castle");
    clearing.setName("Clearing");
    hall.setName("Hall");
    garden.setName("Garden");
    library.setName("Library");
    forest.setName("Forest");
    house.setName("House");
    ruins.setName("Ruins");
    field.setName("Field");

    // Set the descriptions for each location
    cave.setDescription("You are in a dark cave. You can see a faint light to the east.");
    temple.setDescription("You are in an ancient temple. The walls are covered in moss and ivy.");
    dungeon.setDescription("You are in a dark dungeon. You can hear the sound of dripping water.");
    castle.setDescription("You are in a grand castle. The walls are adorned with tapestries.");
    clearing.setDescription("You are in a clearing in the forest. The sun is shining.");
    hall.setDescription("You are in a grand hall. The room is filled with the sound of music.");
    garden.setDescription("You are in a beautiful garden. The flowers are in full bloom.");
    library.setDescription("You are in a dusty library. The shelves are filled with old books.");
    forest.setDescription("You are in a dense forest. The trees are tall and imposing.");
    house.setDescription("You are in a small house. The fire is crackling in the hearth.");
    ruins.setDescription("You are in a ruined building. The roof has collapsed in places.");
    field.setDescription("You are in a field. The grass is swaying in the breeze.");

    // Add items to the locations
    cave.addItem(&emerald);
    temple.addItem(&diamond);
    temple.addItem(&sword);
    dungeon.addItem(&redHealing);
    castle.addItem(&goldRing);
    castle.addItem(&stick);
    clearing.addItem(&club);
    hall.addItem(&bagOfCoins);
    hall.addItem(&blueHealing);
    garden.addItem(&ruby);
    garden.addItem(&crossbow);
    house.addItem(&treasureChest);
    ruins.addItem(&purpleHealing);
    ruins.addItem(&pearl);
    library.addItem(&book);
    library.addItem(&cup);
    field.addItem(&sapphire);
    field.addItem(&dagger);

    // Add monsters to the locations
    field.addMonster(&goblin);
    dungeon.addMonster(&zombie);
    forest.addMonster(&banshee);
    castle.addMonster(&vampire);
    ruins.addMonster(&dragon);
    house.addMonster(&orc);
    house.addMonster(&spectre);
    garden.addMonster(&ghoul);

    ghoul.setLoot(&key);

    // Add armours to the locations
    library.addItem(&gauntlet);
    dungeon.addItem(&helmet);
    clearing.addItem(&breastplate);
    ruins.addItem(&shield);
    house.addItem(&chainmail);
    garden.addItem(&ringmail);
}

// Function to create the map of locations
void CreateMap() {
    cave.addExit(EAST, &field);

    field.addExit(WEST, &cave);
    field.addExit(EAST, &forest);
    field.addExit(SOUTH, &dungeon);

    dungeon.addExit(NORTH, &field);
    dungeon.addExit(EAST, &castle);

    castle.addExit(WEST, &dungeon);
    castle.addExit(SOUTH, &ruins);
    castle.addExit(NORTH, &forest);

    ruins.addExit(NORTH, &castle);

    forest.addExit(SOUTH, &castle);
    forest.addExit(WEST, &field);
    forest.addExit(NORTH, &temple);

    temple.addExit(SOUTH, &forest);
    temple.addExit(EAST, &clearing);

    clearing.addExit(WEST, &temple);
    clearing.addExit(EAST, &house);

    house.addExit(WEST, &clearing);
    house.addExit(EAST, &library);
    house.addExit(SOUTH, &hall);

    library.addExit(WEST, &house);
    library.addExit(SOUTH, &garden);

    garden.addExit(NORTH, &library);
    garden.addExit(WEST, &hall);

    hall.addExit(NORTH, &house);
    hall.addExit(EAST, &garden);

    // Get the exits for each location
    cave.getExits();
    temple.getExits();
    dungeon.getExits();
    castle.getExits();
    clearing.getExits();
    hall.getExits();
    garden.getExits();
    library.getExits();
    forest.getExits();
    house.getExits();
    ruins.getExits();
    field.getExits();
}

// Function to initialise the player
void InitPlayer(){
    player.setName("Player");
    player.setScore(100);
    player.setHitPoints(20);
    
    player.setCurrentLocation(clearing);
    AvaliableExits = player.getCurrentLocation().getExits();
}

// Function to initialise the boss
void InitBoss(){
    boss.setName("Boss");
    boss.setHitPoints(30);

    boss.setCurrentLocation(cave);
}

// Function to try to move the player in a specified direction
void TryMove(Direction direction){
    // Check if the specified direction is in the list of available exits
    if(AvaliableExits.find(direction) != AvaliableExits.end()){
        // If it is, move the player to the location in that direction
        player.setCurrentLocation(*AvaliableExits[direction]);

        // Update the list of available exits based on the player's new location
        AvaliableExits = player.getCurrentLocation().getExits();
    }
    else{
        // If the specified direction is not in the list of available exits, print a message
        cout << "You cannot move in that direction." << endl;
    }
}

// Function to show the player's inventory
void ShowInventory(){
    cout << "===== Inventory ===== " << endl;

    // Print the list of weapons
    cout << "Weapons: " << endl;
    // Check if the player's weapon list is empty
    if(player.weapons.empty()){
        // If it is, print "None"
        cout << "None" << endl;
    }
    else{
        // If it is not, loop through each weapon and print its name and power
        for(Weapon weapon : player.weapons){
            cout << weapon.getName() << " (" << weapon.getPower() << " Power)" << endl;
        }
    }

    // Print the list of potions
    cout << "Potions: " << endl;
    // Check if the player's potion list is empty
    if(player.potions.empty()){
        // If it is, print "None"
        cout << "None" << endl;
    }
    else{
        // If it is not, loop through each potion and print its name and strength
        for(Potion potion : player.potions){
            cout << potion.getName() << " (" << potion.getStrength() << " Strength)" << endl;
        }
    }

    // Print the list of treasures
    cout << "Treasures: " << endl;
    // Check if the player's treasure list is empty
    if(player.treasures.empty()){
        // If it is, print "None"
        cout << "None" << endl;
    }
    else{
        // If it is not, loop through each treasure and print its name and value
        for(Treasure treasure : player.treasures){
            cout << treasure.getName() << " (" << treasure.getValue() << " Value)" << endl;
        }
    }

    // Print the list of armours
    cout << "Armour: " << endl;
    // Check if the player's armour list is empty
    if(player.getArmour().empty()){
        // If it is, print "None"
        cout << "None" << endl;
    }
    else{
        // If it is not, loop through each armour and print its name and protection
        for(Armour armour : player.getArmour()){
            cout << armour.getName() << " (" << armour.getProtection() << " Protection)" << endl;
        }
    }

    cout << "=====================" << endl;
}

// Function to show the player's status
void ShowPlayerStatus(){
    cout << "===== Player Status =====" << endl;

    // Print the player's name
    cout << "Player: " << player.getName() << endl;
    // Print the player's hit points
    cout << "Hit Points: " << player.getHitPoints() << endl;
    // Print the player's score
    cout << "Score: " << player.getScore() << endl;
    cout << "=========================" << endl;
}

// Function to collect items from the player's current location
void CollectItems(){
    // Get the lists of weapons, potions, treasures, and armours in the player's current location
    vector<Weapon*> weapons = player.getCurrentLocation().weapons;
    vector<Potion*> potions = player.getCurrentLocation().potions;
    vector<Treasure*> treasures = player.getCurrentLocation().treasure;
    vector <Armour*> armours = player.getCurrentLocation().armours;

    // initialise a counter for the number of items collected
    int itemsCollectedCount = 0;

    // Loop through each weapon in the location
    for(Weapon* weapon : weapons){
        // Add the weapon to the player's weapon list
        player.weapons.push_back(*weapon);
        // Set the weapon's availability to false
        weapon->setAvailability(false);
        // Increment the item collected count
        itemsCollectedCount++;
    }

    // Loop through each potion in the location
    for(Potion* potion : potions){
        // Add the potion to the player's potion list
        player.potions.push_back(*potion);
        // Set the potion's availability to false
        potion->setAvailability(false);
        // Increment the item collected count
        itemsCollectedCount++;
    }

    // Loop through each treasure in the location
    for(Treasure* treasure : treasures){
        // Add the treasure to the player's treasure list
        player.treasures.push_back(*treasure);
        // Increase the player's score by the value of the treasure
        player.setScore(player.getScore() + treasure->getValue());
        // Set the treasure's availability to false
        treasure->setAvailability(false);
        // Increment the item collected count
        itemsCollectedCount++;
    }

    // Loop through each armour in the location
    for (Armour* armour : armours) {
        // Add the armour to the player's armour list
        player.addArmour(*armour);
        // Set the armour's availability to false
        armour->setAvailability(false);
        // Increment the item collected count
        itemsCollectedCount++;
    }

    // Print a message indicating how many items were collected
    cout << "You have collected " << itemsCollectedCount << " item/items from the location." << endl;
}
// Function to drink a potion
void DrinkPotion(){
    // Check if the player's potion list is empty
    if(player.potions.empty()){
        // If it is, print a message and return from the function
        cout << "You don't have any potions to drink." << endl;
        return;
    }
    // Get the last potion in the player's potion list
    Potion& potion = player.potions.back();
    // Increase the player's hit points by the strength of the potion
    player.setHitPoints(player.getHitPoints() + potion.getStrength());
    // Remove the potion from the player's potion list
    player.potions.pop_back();
    // Print a message indicating the player drank the potion and how many hit points were restored
    cout << "You drank a " << potion.getName() << " and restored " << potion.getStrength() << " hit points." << endl;
}


// Function to select a monster to fight
Monster SelectMonsterToFight(){
    // Get the list of monsters in the player's current location
    vector<Monster*> monsters = player.getCurrentLocation().getMonsters();

    // Initially select the first monster in the list
    Monster selectedMonster = *monsters[0];

    // Loop through each monster in the list
    for (Monster* monster : monsters){
        // If the current monster has more hit points than the currently selected monster
        if (monster->getHitPoints() > selectedMonster.getHitPoints()){
            // Select the current monster
            selectedMonster = *monster;
        }
    }

    // Return the selected monster
    return selectedMonster;
}