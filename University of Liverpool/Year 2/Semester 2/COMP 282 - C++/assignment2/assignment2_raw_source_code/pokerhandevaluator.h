#ifndef POKERHANDEVALUATOR_H
#define POKERHANDEVALUATOR_H

#include "hand.h"
#include <QVector>

// The PokerHandEvaluator class evaluates poker hands.
class PokerHandEvaluator {
public:
    // Default constructor for the PokerHandEvaluator class.
    PokerHandEvaluator();

    // Evaluates the strength of a single hand.
    int evaluate(const Hand &hand) const;

    // Compares two hands to determine which is stronger.
    // Returns 1 if hand1 is stronger, -1 if hand2 is stronger, and 0 if they are equal.
    int compare(const Hand &hand1, const Hand &hand2) const;

    // Returns the type of the hand as a string.
    QString getHandType(const Hand &hand) const;

    // Sorts cards by rank in descending order for easier evaluation.
    void sortByRank(QVector<Card> &cards) const;

    // Helper functions to evaluate specific types of poker hands.
    bool isStraight(const QVector<Card> &cards) const;
    bool isFlush(const QVector<Card> &cards) const;
    bool isStraightFlush(const QVector<Card> &cards) const;
    bool isFourOfAKind(const QVector<Card> &cards) const;
    bool isFullHouse(const QVector<Card> &cards) const;
    bool isThreeOfAKind(const QVector<Card> &cards) const;
    bool isTwoPair(const QVector<Card> &cards) const;
    bool isPair(const QVector<Card> &cards) const;

private:

};

#endif // POKERHANDEVALUATOR_H
