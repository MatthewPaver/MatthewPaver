#ifndef PLAYER_H
#define PLAYER_H

#include <QVector>
#include "card.h"
#include "pokerhandevaluator.h"

// The Player class represents a player in the game.
class Player {
public:
    // Default constructor for the Player class.
    Player();

    // Adds a card to the player's hand.
    void addCard(const Card &card);

    // Clears the player's hand of cards.
    void clearHand();

    // Replaces a card at a specific index in the player's hand.
    void replaceCard(int index, const Card &newCard);

    // Returns the player's current hand of cards.
    QVector<Card> getHand() const;

    // Calculates the score of the player's hand based on poker rules.
    int calculateScore() const;

private:
    // Vector to store the player's current hand of cards.
    QVector<Card> hand;
};

#endif // PLAYER_H
