#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QCheckBox>
#include "game.h"

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

// The MainWindow class represents the main window of the application.
class MainWindow : public QMainWindow {
    Q_OBJECT

    // Forward declaration of Rank from the Card class
    enum class Rank;

    // Declaration of the rankToString function
    QString rankToString(Rank rank);

public:
    // Constructor and destructor for the MainWindow class
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

    // Vector to store the indices of selected cards
    QVector<int> selectedCardIndices;

    // Clears the selection of cards
    void clearCardSelections();

    // Finishes the game and displays the final scores
    void finishGame();

    // Resets the game to its initial state
    void resetGame();

private slots:
    // Starts a new game
    void startGame();

    // Proceeds to the next round of the game
    void nextRound();

    // Swaps the selected cards in the player's hand
    void swapCards();

    // Checks the player's hand and updates the score
    void checkHand();

    // Updates the displayed scores
    void updateScores(int playerScore, int computerScore);

    // Updates the displayed cards
    void updateCards();

    // Updates the display of remaining cards in the deck
    void updateRemainingCards();

    // Handles the end of a round and displays the winner
    void handleRoundWinner(const QString &winner);

    // Disables the button to proceed to the next round
    void disableNextRoundButton();

private:
    Ui::MainWindow *ui;
    Game *game;  // Instance of the Game class to manage game logic

    int previousPlayerScore = 0;  // Initialize score tracking
    int previousComputerScore = 0;

    int totalPlayerScore;
    int totalComputerScore;

    // Displays a hand of cards at the specified coordinates
    void displayHand(const QVector<Card>& hand, qreal x, qreal y, bool isPlayer);

    // Connects UI elements to slots
    void setupUiConnections();
};

#endif // MAINWINDOW_H
