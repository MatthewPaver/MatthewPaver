#include "player.h"
#include "pokerhandevaluator.h"

// Constructor for the Player class
Player::Player() {
    // Constructor might initialize other elements if necessary
}

// Method to add a card to the player's hand
void Player::addCard(const Card &card) {
    hand.append(card);  // Add a new card to the hand
}

// Method to clear the player's hand
void Player::clearHand() {
    hand.clear();  // Clear all cards from the hand
}

// Method to replace a card in the player's hand
void Player::replaceCard(int index, const Card &newCard) {
    if (index >= 0 && index < hand.size()) {
        hand[index] = newCard;  // Replace the card at the specified index
    }
}

// Method to get the player's hand
QVector<Card> Player::getHand() const {
    return hand;  // Return the current hand of the player
}

// Method to calculate the player's score
int Player::calculateScore() const {
    PokerHandEvaluator evaluator;
    return evaluator.evaluate(Hand(hand));  // Evaluate the hand and return the score
}
