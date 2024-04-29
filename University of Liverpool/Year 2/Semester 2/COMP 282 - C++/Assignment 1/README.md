# Adventure Game README

## Overview
This repository contains a C++ project designed for the command-line interface. It's a fantasy-themed adventure game, inspired by classic games like Dungeons and Dragons, where players navigate through various locations, collect items, fight monsters, and aim to defeat the end-level boss to achieve the highest score.

### Main Components
- **Character** - Base class for all characters (Player, Monster).
- **Item** - Base class for all items (Weapon, Potion, Treasure, Armour).
- **Location** - Represents different locations in the game world.
- **Player** - Derived from Character, represents the user's avatar in the game.
- **Monster** - Derived from Character, represents various adversaries in the game.
- **Weapon, Potion, Treasure, Armour** - Specific item classes derived from Item.

## Prerequisites
To build and run this game, you will need:
- C++ Compiler supporting C++14 (e.g., GCC, Clang, MSVC)
- Makefile or an IDE that supports C++ projects (optional for build configuration)
