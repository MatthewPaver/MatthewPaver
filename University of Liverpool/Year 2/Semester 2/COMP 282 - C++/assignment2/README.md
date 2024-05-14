
# Card Game - Poker Style

## Introduction
This project is a GUI-based card game developed using C++ with the Qt framework. It simulates a poker-like game where the objective is to beat a computer opponent using a standard 52-card deck. The game incorporates Object-Oriented Programming (OOP) methods to organize its structure.

Royalty-free card images, representing all 52 standard playing cards, are used in the game. These images can be downloaded from the COMP282 Canvas page and should be placed in the application's output directory.

If you're new to the concept of a standard 52-card deck, more details can be found on [Wikipedia](https://en.wikipedia.org/wiki/Standard_52-card_deck).

## Setup Instructions
1. **Download Card Images**: Obtain the 52 PNG images of standard playing cards from the COMP282 Canvas page. Place these images in a directory named `playing_cards` within the application's output directory.
  
2. **Compile the Game**: Ensure Qt development environment is set up with C++. Compile the source code using the appropriate Qt compiler settings.

3. **Run the Application**: Launch the compiled executable. The main window will prompt you to start the game.

## Game Rules
### Objective
Beat the computer opponent by forming combinations of 5 cards (a Hand) with the highest value.

### Card Values and Suits
- **Values**: Cards range from 1 to 14. Aces can be low (1) or high (14), useful in forming straights. Numbered cards are worth their face value, and Jacks, Queens, Kings are valued at 11, 12, and 13 respectively.
- **Suits**: Hearts (♥), Diamonds (♦), Spades (♠), and Clubs (♣). Suits are only relevant for determining a Flush.

### Hand Rankings
1. **Straight Flush**: A sequence with all cards in the same suit.
2. **Four of a Kind**: Four cards of the same value.
3. **Full House**: Three cards of one value and two cards of another value.
4. **Flush**: All cards are of the same suit.
5. **Straight**: All cards are in numerical order, regardless of suit.
6. **Three of a Kind**: Three cards of the same value.
7. **Two Pair**: Two sets of pairs of different values.
8. **One Pair**: Two cards of the same value.
9. **High Card**: The highest card in the hand if no other combinations are present.

### Determining Winners
- If both players have the same hand type, the highest cards are compared. If these are equal, the next highest cards are considered, and so on.
- Specific rules for ties in each hand type (like Straight Flush, Four of a Kind, etc.) are detailed in the introduction section.

## Development Notes
- Ensure the images folder is correctly placed relative to the application's executable for successful image loading.
- The game uses OOP principles with classes like `Game`, `Player`, `Card`, `Deck`, and `Hand` to encapsulate the logic.

## License
This project is for educational purposes under the guidance of the COMP282 curriculum.

## Support
For any issues or suggestions, please refer to the course instructor or the teaching assistants.

