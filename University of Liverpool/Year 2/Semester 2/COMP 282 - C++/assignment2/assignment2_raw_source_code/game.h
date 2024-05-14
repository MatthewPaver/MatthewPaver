#ifndef GAME_H
#define GAME_H

#include <QObject>
#include <QVector>
#include "card.h"
#include "player.h"
#include "deck.h"  // Ensure this class is defined to manage a deck of cards

// The Game class represents a game of cards.
class Game : public QObject {
    Q_OBJECT

public:
    Deck deck;  // The deck of cards for the game

    // Initializes or resets the game components
    void initializeGame();

    // Accessors for the players
    Player* getPlayer1();
    Player* getPlayer2();

    // Determines which cards the computer player should swap
    QVector<int> getComputerSwapIndices();

    // Determines the winner of a round and returns a message
    QString determineRoundWinnerMessage(int playerScore, int computerScore);

    // Deals initial hands to the players
    void dealHands();

    // Constructor for the Game class
    explicit Game(QObject *parent = nullptr, QWidget *mainWidget = nullptr);

    // Starts the entire game, shuffles the deck, and deals initial hands
    void startGame();

    // Proceeds to the next round by dealing new hands
    void nextRound();

    int swapCount = 0; // Tracks the number of swaps in the current round

    // Allows a player to swap cards from their hand
    void swapCards(Player &player, const QVector<int> &cardIndices);

    // Retrieves scores for UI display
    int getPlayerScore(const Player &player) const;
    int getComputerScore() const;
    int getPlayerScore() const;

    // Retrieves current hands for UI display
    QVector<Card> getPlayerHand() const;
    QVector<Card> getComputerHand() const;

    // Retrieves the current round number
    int getCurrentRound() const;

    // Evaluates hands at the end of each round to update scores
    void evaluateHands();

    // Shuffles the deck of cards
    void shuffleDeck();

    // Resets the players' hands and any necessary states
    void resetPlayers();

signals:
    // Signals to update UI based on game state changes
    void gameStarted();
    void roundStarted();
    void scoresUpdated(int playerScore, int computerScore);
    void cardsUpdated();
    void roundWinner(const QString &winner);
    void disableNextRoundButton();

private:
    int currentRound;  // Tracks the current round number
    QWidget* mainWidget; // Store the main widget
    Player player1;  // Represents the human player
    Player player2;  // Represents the computer opponent
    int totalPlayerScore = 0;  // Total score for the player
    int totalComputerScore = 0;  // Total score for the computer
};

#endif // GAME_H
