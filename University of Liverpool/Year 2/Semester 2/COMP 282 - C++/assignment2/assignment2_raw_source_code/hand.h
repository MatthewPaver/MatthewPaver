#ifndef HAND_H
#define HAND_H

#include <QVector>
#include "card.h"

// The Hand class represents a hand of cards.
class Hand {
public:
    // Default constructor for the Hand class.
    Hand();

    // Constructor that initializes the hand with a given set of cards.
    Hand(const QVector<Card>& cards) {
        // Initialize the hand with the cards from the QVector
        for (const Card& card : cards) {
            // Add each card to the hand
            addCard(card);
        }
    }

    // Replaces a card at a specific index with a new card.
    void replaceCard(int index, const Card &newCard);

    // Adds a card to the hand.
    void addCard(const Card &card);

    // Removes a card from the hand at a specific index.
    void removeCard(int index);

    // Returns the number of cards in the hand.
    int size() const;

    // Returns the cards currently in the hand.
    QVector<Card> getCards() const;

    // Evaluates the strength of the hand based on poker rules.
    int evaluateHand() const;

private:
    // Vector to store the cards in the hand.
    QVector<Card> cards;
};

#endif // HAND_H
