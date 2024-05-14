#include "deck.h"

// Default constructor for Deck
Deck::Deck() {
    // Initialize the deck when a Deck object is created
    initializeDeck();
}

// Getter for cards
QVector<Card>& Deck::getCards() {
    return cards;
}

// Method to initialize the deck
void Deck::initializeDeck() {
    cards.clear();  // Clear the current deck
    QString basePath = "";
    QVector<QString> suits = {"clubs", "diamonds", "hearts", "spades"};
    QVector<QString> ranks = {"ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"};

    // Loop through each suit and rank to create a card
    for (int s = 0; s < suits.size(); ++s) {
        for (int r = 0; r < ranks.size(); ++r) {
            QString imagePath = basePath + ranks[r] + "_of_" + suits[s] + ".png";
            cards.append(Card(static_cast<Suit>(s), static_cast<Rank>(r + 1), imagePath));
        }
    }
}

// Method to shuffle the deck
void Deck::shuffle() {
    auto seed = QRandomGenerator::global()->generate();
    std::shuffle(cards.begin(), cards.end(), QRandomGenerator(seed));
}

// Method to deal a card
Card Deck::dealCard() {
    if (!cards.isEmpty()) {
        return cards.takeFirst(); // Removes and returns the first card in the deck
    }
    return Card(Suit::Clubs, Rank::Ace, ""); // Return a default card if no more cards are left
}

// Method to peek a card at a specific index
Card Deck::peekCard(int index) const {
    if (index >= 0 && index < cards.size()) {
        return cards[index];
    }
    return Card(); // Return a default card if the index is out of bounds
}
