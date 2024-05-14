#include "pokerhandevaluator.h"
#include <algorithm>

// Constructor for the PokerHandEvaluator class
PokerHandEvaluator::PokerHandEvaluator() {}

// Method to evaluate a hand and return a score
int PokerHandEvaluator::evaluate(const Hand &hand) const {
    QVector<Card> cards = hand.getCards();
    sortByRank(cards);

    // Check for different types of hands, from highest to lowest
    if (isStraightFlush(cards)) return 9;
    if (isFourOfAKind(cards)) return 8;
    if (isFullHouse(cards)) return 7;
    if (isFlush(cards)) return 6;
    if (isStraight(cards)) return 5;
    if (isThreeOfAKind(cards)) return 4;
    if (isTwoPair(cards)) return 3;
    if (isPair(cards)) return 2;

    return 1;  // High card evaluation
}

// Method to compare two hands and return a result
int PokerHandEvaluator::compare(const Hand &hand1, const Hand &hand2) const {
    int score1 = evaluate(hand1);
    int score2 = evaluate(hand2);

    // If the scores are equal, compare the individual cards
    if (score1 == score2) {
        QVector<Card> cards1 = hand1.getCards(), cards2 = hand2.getCards();
        sortByRank(cards1);
        sortByRank(cards2);

        // Compare each card in the hand
        for (int i = 0; i < cards1.size(); ++i) {
            if (cards1[i].getRank() > cards2[i].getRank()) return 1;
            if (cards1[i].getRank() < cards2[i].getRank()) return -1;
        }
        return 0;  // Tie if all cards match
    }
    return score1 > score2 ? 1 : -1;
}

// Method to check if a hand is a straight
bool PokerHandEvaluator::isStraight(const QVector<Card> &cards) const {
    QVector<int> values;
    for (const Card &card : cards) {
        values.append(static_cast<int>(card.getRank()));
    }
    std::sort(values.begin(), values.end());

    // Check for low Ace straight
    if (values.contains(14)) {
        values.prepend(1);  // Treat Ace as 1 as well
    }

    // Check if the values are sequential
    for (int i = 0; i <= values.size() - 5; ++i) {
        bool isSequential = true;
        for (int j = 1; j < 5; ++j) {
            if (values[i + j] != values[i] + j) {
                isSequential = false;
                break;
            }
        }
        if (isSequential) return true;
    }
    return false;
}

// Method to check if a hand is a flush
bool PokerHandEvaluator::isFlush(const QVector<Card> &cards) const {
    Suit suit = cards[0].getSuit();
    for (const Card &card : cards) {
        if (card.getSuit() != suit) return false;
    }
    return true;
}

// Method to check if a hand is a straight flush
bool PokerHandEvaluator::isStraightFlush(const QVector<Card> &cards) const {
    return isStraight(cards) && isFlush(cards);
}

// Method to check if a hand is a four of a kind
bool PokerHandEvaluator::isFourOfAKind(const QVector<Card> &cards) const {
    int count = 1;
    for (int i = 1; i < cards.size(); ++i) {
        if (cards[i].getRank() == cards[i-1].getRank()) {
            ++count;
        } else {
            if (count == 4) return true;
            count = 1;
        }
    }
    return count == 4;  // Check the last group
}

// Method to check if a hand is a full house
bool PokerHandEvaluator::isFullHouse(const QVector<Card> &cards) const {
    bool three = false, two = false;
    int count = 1;
    for (int i = 1; i < cards.size(); ++i) {
        if (cards[i].getRank() == cards[i-1].getRank()) {
            ++count;
        } else {
            if (count == 3) three = true;
            else if (count == 2) two = true;
            count = 1;
        }
    }
    return (count == 3 && two) || (three && count == 2);  // Full House check
}

// Method to check if a hand is a three of a kind
bool PokerHandEvaluator::isThreeOfAKind(const QVector<Card> &cards) const {
    int count = 1;
    for (int i = 1; i < cards.size(); ++i) {
        if (cards[i].getRank() == cards[i-1].getRank()) {
            ++count;
        } else {
            if (count == 3) return true;
            count = 1;
        }
    }
    return count == 3;  // Check the last group
}

// Method to check if a hand is a two pair
bool PokerHandEvaluator::isTwoPair(const QVector<Card> &cards) const {
    int pairs = 0, count = 1;
    for (int i = 1; i < cards.size(); ++i) {
        if (cards[i].getRank() == cards[i-1].getRank()) {
            ++count;
        } else {
            if (count == 2) pairs++;
            count = 1;
        }
    }
    return pairs == 2 || (count == 2 && pairs == 1);  // Two Pair check
}

// Method to check if a hand is a pair
bool PokerHandEvaluator::isPair(const QVector<Card> &cards) const {
    int count = 1;
    for (int i = 1; i < cards.size(); ++i) {
        if (cards[i].getRank() == cards[i-1].getRank()) {
            ++count;
        } else {
            if (count == 2) return true;
            count = 1;
        }
    }
    return count == 2;  // Check the last group
}

// Method to sort cards by rank
void PokerHandEvaluator::sortByRank(QVector<Card> &cards) const {
    std::sort(cards.begin(), cards.end(), [](const Card &a, const Card &b) {
        return a.getRank() > b.getRank();
    });
}

QString PokerHandEvaluator::getHandType(const Hand &hand) const {
    QVector<Card> cards = hand.getCards();
    sortByRank(cards);

    if (isStraightFlush(cards)) return "Straight Flush";
    if (isFourOfAKind(cards)) return "Four of a Kind";
    if (isFullHouse(cards)) return "Full House";
    if (isFlush(cards)) return "Flush";
    if (isStraight(cards)) return "Straight";
    if (isThreeOfAKind(cards)) return "Three of a Kind";
    if (isTwoPair(cards)) return "Two Pair";
    if (isPair(cards)) return "One Pair";

    return "High Card";  // Default for no matched combination
}
