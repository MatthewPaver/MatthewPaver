#include "game.h"
#include "pokerhandevaluator.h"
#include <QDebug>
#include <QMessageBox>
#include <QApplication>

// Constructor for the Game class
Game::Game(QObject *parent, QWidget *mainWidget)
: QObject(parent), currentRound(0), mainWidget(mainWidget) {
    // Initialize or reset the game upon creation
    initializeGame();
}

// Method to initialize the game
void Game::initializeGame() {
    // Reset the game state, shuffle the deck, and prepare players
    deck.shuffle();
    player1.clearHand();
    player2.clearHand();
    currentRound = 1;
    totalPlayerScore = 0; // Reset total score for the player
    totalComputerScore = 0; // Reset total score for the computer
    emit roundStarted();
}

// Method to start the game
void Game::startGame() {
    qDebug() << "Starting the game";
    currentRound = 1;

    shuffleDeck(); // Use a method if it exists or direct call to deck.shuffle();
    resetPlayers(); // Reset the players' hands
    swapCount = 0;  // Reset swap count for the new game

    // Deal initial cards to both players
    for (int i = 0; i < 5; ++i) {
        Card newCard = deck.dealCard();
        newCard.setShow(true);  // Ensure the front is visible for player1
        player1.addCard(newCard);

        newCard = deck.dealCard();
        newCard.setShow(true);  // Ensure the front is visible for player2
        player2.addCard(newCard);
    }

    emit gameStarted();
    emit scoresUpdated(getPlayerScore(player1), getComputerScore());
    emit cardsUpdated();
}

// Method to proceed to the next round
void Game::nextRound() {
    if (deck.remainingCards() < 10) {
        QMessageBox::information(mainWidget, "Game Over", "Not enough cards to continue.");
        emit disableNextRoundButton();  // Emit a new signal to inform the UI
        return;
    }
    currentRound++;
    dealHands();
    evaluateHands();
    emit scoresUpdated(getPlayerScore(), getComputerScore());
    emit roundStarted();
    emit cardsUpdated();
}

// Method to swap cards for a player
void Game::swapCards(Player &player, const QVector<int> &cardIndices) {
    QVector<Card> swappedOut;
    for (int index : cardIndices) {
        if (index < player.getHand().size()) {
            swappedOut.append(player.getHand()[index]);
            Card newCard = deck.dealCard();
            newCard.setShow(true);
            player.replaceCard(index, newCard);
        }
    }

    // Shuffle swapped-out cards back into the deck
    for (Card &card : swappedOut) {
        deck.getCards().insert(QRandomGenerator::global()->bounded(deck.remainingCards() + 1), card);
    }
    deck.shuffle();

    evaluateHands();
    emit scoresUpdated(getPlayerScore(), getComputerScore());
    emit cardsUpdated();
}

// Method to get the score of a player
int Game::getPlayerScore(const Player &player) const {
    return player.calculateScore();  // Assume Player class has a method to calculate score
}

// Method to get the hand of cards for player1
QVector<Card> Game::getPlayerHand() const {
    return player1.getHand();
}

// Method to get the hand of cards for player2
QVector<Card> Game::getComputerHand() const {
    return player2.getHand();
}

// Method to evaluate the hands of both players
void Game::evaluateHands() {
    PokerHandEvaluator evaluator;
    QVector<Card> playerCards = player1.getHand();
    QVector<Card> computerCards = player2.getHand();

    // Sort cards to facilitate hand comparisons
    evaluator.sortByRank(playerCards);
    evaluator.sortByRank(computerCards);

    int playerScore = evaluator.evaluate(Hand(playerCards));
    int computerScore = evaluator.evaluate(Hand(computerCards));

    QString resultMessage;
    // Compare the scores to decide the round winner
    if (playerScore > computerScore) {
        totalPlayerScore++;
        resultMessage = "Player wins the round with " + PokerHandEvaluator().getHandType(Hand(playerCards)) +
                        " over " + PokerHandEvaluator().getHandType(Hand(computerCards));
        emit roundWinner("player");
    } else if (computerScore > playerScore) {
        totalComputerScore++;
        resultMessage = "Computer wins the round with " + PokerHandEvaluator().getHandType(Hand(computerCards)) +
                        " over " + PokerHandEvaluator().getHandType(Hand(playerCards));
        emit roundWinner("computer");
    } else {
        // Use high card tie-breaker for same score hands like One Pair vs One Pair
        QVector<Card> sortedPlayerCards = playerCards;
        QVector<Card> sortedComputerCards = computerCards;
        std::sort(sortedPlayerCards.begin(), sortedPlayerCards.end(), [](const Card& a, const Card& b) {
            return a.getRank() > b.getRank();
        });
        std::sort(sortedComputerCards.begin(), sortedComputerCards.end(), [](const Card& a, const Card& b) {
            return a.getRank() > b.getRank();
        });

        int i = 0;
        while (i < sortedPlayerCards.size() && sortedPlayerCards[i].getRank() == sortedComputerCards[i].getRank()) {
            i++;
        }
        if (i < sortedPlayerCards.size()) {
            if (sortedPlayerCards[i].getRank() > sortedComputerCards[i].getRank()) {
                totalPlayerScore++;
                resultMessage = "Tie broken by Player with higher card " + rankToString(sortedPlayerCards[i].getRank()) +
                                " over " + rankToString(sortedComputerCards[i].getRank());
                emit roundWinner("player");
            } else {
                totalComputerScore++;
                resultMessage = "Tie broken by Computer with higher card " + rankToString(sortedComputerCards[i].getRank()) +
                                " over " + rankToString(sortedPlayerCards[i].getRank());
                emit roundWinner("computer");
            }
        } else {
            resultMessage = "The round ends in a draw.";
            emit roundWinner("tie");
        }
    }

    QMessageBox::information(mainWidget, "Round Result", determineRoundWinnerMessage(playerScore, computerScore) + "\n" + resultMessage);
    emit scoresUpdated(totalPlayerScore, totalComputerScore);
}

// Method to get the total score of player1
int Game::getPlayerScore() const {
    return totalPlayerScore;
}

// Method to get the total score of player2
int Game::getComputerScore() const {
    return totalComputerScore;
}

// Method to get the indices of cards that the computer player wants to swap
QVector<int> Game::getComputerSwapIndices() {
    QVector<int> indicesToSwap;
    Hand computerHand = player2.getHand();
    int scoreBefore = PokerHandEvaluator().evaluate(computerHand);

    // Iterate over each card in the computer's hand
    for (int i = 0; i < computerHand.size(); ++i) {
        int bestImprovement = scoreBefore;
        int bestIndex = -1;
        // Iterate over each remaining card in the deck
        for (int j = 0; j < deck.remainingCards(); ++j) {
            if (j >= deck.remainingCards()) break;
            Hand hypotheticalHand = computerHand;
            Card hypotheticalCard = deck.peekCard(j);
            hypotheticalHand.replaceCard(i, hypotheticalCard);
            int scoreAfter = PokerHandEvaluator().evaluate(hypotheticalHand);

            // If the score improves by swapping the card, remember the index
            if (scoreAfter > bestImprovement) {
                bestImprovement = scoreAfter;
                bestIndex = j;
            }
        }
        // If an improvement was found, add the index to the swap list
        if (bestIndex != -1) indicesToSwap.append(i);
        if (indicesToSwap.size() >= 3) break;  // Limit to 3 swaps
    }
    return indicesToSwap;
}

// Method to get a pointer to player1
Player* Game::getPlayer1() {
    return &player1;
}

// Method to get a pointer to player2
Player* Game::getPlayer2() {
    return &player2;
}

// Method to get the current round number
int Game::getCurrentRound() const {
    return currentRound;
}

// Method to shuffle the deck
void Game::shuffleDeck() {
    deck.shuffle(); // Shuffle the deck using the method from the Deck class.
}

// Method to reset the players
void Game::resetPlayers() {
    player1.clearHand(); // Clear the hand for player 1.
    player2.clearHand(); // Clear the hand for player 2.
    // Reset other necessary states if needed, e.g., scores.
    totalPlayerScore = 0;
    totalComputerScore = 0;
}

// Method to deal hands to both players
void Game::dealHands() {
    player1.clearHand(); // Clear the hand for player 1.
    player2.clearHand(); // Clear the hand for player 2.
    // Deal 5 cards to each player
    for (int i = 0; i < 5; ++i) {
        Card newCard = deck.dealCard(); // Deal a card from the deck
        newCard.setShow(true); // Set the card to be visible
        player1.addCard(newCard); // Add the card to player 1's hand

        newCard = deck.dealCard(); // Deal another card from the deck
        newCard.setShow(true); // Set the card to be visible
        player2.addCard(newCard); // Add the card to player 2's hand
    }
}

// Method to determine the winner of the round and return a message
QString Game::determineRoundWinnerMessage(int playerScore, int computerScore) {
    if (playerScore > computerScore) {
        return "Player wins the round!"; // Player 1 wins
    } else if (computerScore > playerScore) {
        return "Computer wins the round!"; // Player 2 wins
    }
    return "The round ends in a draw."; // It's a draw
}
