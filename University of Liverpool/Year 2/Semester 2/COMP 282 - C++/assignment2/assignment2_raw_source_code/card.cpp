#include "card.h"

// Function to convert Rank enum to string
QString rankToString(Rank rank) {
    switch (rank) {
        case Rank::Ace: return "Ace";
        case Rank::Two: return "2";
        case Rank::Three: return "3";
        case Rank::Four: return "4";
        case Rank::Five: return "5";
        case Rank::Six: return "6";
        case Rank::Seven: return "7";
        case Rank::Eight: return "8";
        case Rank::Nine: return "9";
        case Rank::Ten: return "10";
        case Rank::Jack: return "Jack";
        case Rank::Queen: return "Queen";
        case Rank::King: return "King";
        default: return "Unknown";
    }
}

// Method to convert Suit enum to string
QString Card::suitToString(Suit suit) const {
    switch (suit) {
        case Suit::Clubs: return "Clubs";
        case Suit::Diamonds: return "Diamonds";
        case Suit::Hearts: return "Hearts";
        case Suit::Spades: return "Spades";
        default: return "Unknown";
    }
}

// Constructor for Card with suit, rank and image path
Card::Card(Suit suit, Rank rank, const QString &imagePath)
    : suit(suit), rank(rank), imagePath(imagePath), visible(false) {
    if (!imagePath.isEmpty()) {
        image.load(imagePath);  // Load image if path is not empty
    }
}

// Default constructor for Card
Card::Card() : suit(Suit::Clubs), rank(Rank::Ace), imagePath(""), visible(false) {
}

// Getter for suit
Suit Card::getSuit() const {
    return suit;
}

// Getter for rank
Rank Card::getRank() const {
    return rank;
}

// Getter for image
QPixmap Card::getImage() const {
    return image;
}

// Getter for visibility status
bool Card::shouldShow() const {
    return visible;
}

// Setter for visibility status
void Card::setShow(bool show) {
    visible = show;
}

// Getter for image path
QString Card::getImagePath() const {
    return imagePath;
}
