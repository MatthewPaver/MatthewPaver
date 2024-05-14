#ifndef DECK_H
#define DECK_H

#include <QVector>
#include "card.h"
#include <QRandomGenerator>

// The Deck class represents a deck of cards.
class Deck {
public:
    // Default constructor for the Deck class.
    Deck();

    // Initializes the deck with a standard set of 52 playing cards.
    void initializeDeck();

    // Shuffles the deck of cards.
    void shuffle();

    // Deals (removes and returns) the top card from the deck.
    Card dealCard();

    // Returns a reference to the vector of cards in the deck.
    QVector<Card>& getCards();

    // Returns the card at the specified index without removing it from the deck.
    Card peekCard(int index) const;

    // Returns the number of remaining cards in the deck.
    int remainingCards() const {
        return cards.size();
    }

private:
    // Vector to store the cards in the deck.
    QVector<Card> cards;
};

#endif // DECK_H
