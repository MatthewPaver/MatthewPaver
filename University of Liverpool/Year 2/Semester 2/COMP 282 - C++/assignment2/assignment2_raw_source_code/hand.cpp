#include "hand.h"
#include <algorithm>
#include <QMap>
#include "pokerhandevaluator.h"

// Constructor for the Hand class
Hand::Hand() {
    // Initially, the hand is empty
}

// Method to add a card to the hand
void Hand::addCard(const Card &card) {
    cards.append(card);  // Add a new card to the hand
}

// Method to remove a card from the hand
void Hand::removeCard(int index) {
    if (index >= 0 && index < cards.size()) {
        cards.removeAt(index);  // Remove the card at the specified index
    }
}

// Method to get the size of the hand
int Hand::size() const {
    return cards.size();  // Return the number of cards in the hand
}

// Method to get the cards in the hand
QVector<Card> Hand::getCards() const {
    return cards;  // Return the current cards in the hand
}

// Method to evaluate the hand
int Hand::evaluateHand() const {
    if (cards.isEmpty()) return 0;

    // Use PokerHandEvaluator to sort and evaluate the hand
    PokerHandEvaluator evaluator;
    QVector<Card> sortedCards = cards;
    evaluator.sortByRank(sortedCards);

    // Check highest-ranking hands first
    if (evaluator.isStraightFlush(sortedCards)) return 900 + static_cast<int>(sortedCards[0].getRank());
    if (evaluator.isFourOfAKind(sortedCards)) return 800 + static_cast<int>(sortedCards[1].getRank());
    if (evaluator.isFullHouse(sortedCards)) return 700 + static_cast<int>(sortedCards[2].getRank());
    if (evaluator.isFlush(sortedCards)) return 600 + static_cast<int>(sortedCards[0].getRank());
    if (evaluator.isStraight(sortedCards)) return 500 + static_cast<int>(sortedCards[0].getRank());
    if (evaluator.isThreeOfAKind(sortedCards)) return 400 + static_cast<int>(sortedCards[2].getRank());
    if (evaluator.isTwoPair(sortedCards)) {
        int highPairRank = static_cast<int>(sortedCards[1].getRank());
        int lowPairRank = static_cast<int>(sortedCards[3].getRank());
        return 300 + highPairRank * 10 + lowPairRank;
    }
    if (evaluator.isPair(sortedCards)) return 200 + static_cast<int>(sortedCards[1].getRank());

    // High Card
    return static_cast<int>(sortedCards[0].getRank()); // Return the highest card's rank as the score
}

// Method to replace a card in the hand
void Hand::replaceCard(int index, const Card &newCard) {
    if (index >= 0 && index < cards.size()) {
        cards[index] = newCard;  // Replace the card at the specified index
    }
}
