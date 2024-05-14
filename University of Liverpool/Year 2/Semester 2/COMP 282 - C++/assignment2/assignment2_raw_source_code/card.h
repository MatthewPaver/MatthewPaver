#ifndef CARD_H
#define CARD_H

#include <QString>
#include <QPixmap>

// Define the Suit and Rank enums at a global scope to be used within the Card class
enum class Suit {
    Clubs, Diamonds, Hearts, Spades
};

enum class Rank {
    Ace = 1, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King
};

// Function to convert a Rank enum value to its QString representation
QString rankToString(Rank rank);

class Card {
public:
    // Constructor to create a card with a suit, rank, and image path
    Card(Suit suit, Rank rank, const QString &imagePath);
    // Default constructor to create a card with default values
    Card();

    // Getter for the Suit of the card
    Suit getSuit() const;
    // Getter for the Rank of the card
    Rank getRank() const;
    // Getter for the QPixmap image associated with the card
    QPixmap getImage() const;
    // Check if the card's front side should be shown
    bool shouldShow() const;
    // Setter to determine if the card's front side should be shown
    void setShow(bool show);
    // Getter for the image path of the card
    QString getImagePath() const;

    // Convert the Suit of the card to its QString representation
    QString suitToString(Suit suit) const;

private:
    Suit suit;   // The suit of the card (Clubs, Diamonds, Hearts, Spades)
    Rank rank;   // The rank of the card (Ace, Two, Three, ..., King)
    QPixmap image;  // The image representing the card
    QString imagePath;  // The file path to the image of the card
    bool visible;   // Flag to indicate if the card's front side is visible
};

#endif // CARD_H
