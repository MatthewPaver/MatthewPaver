#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "card.h"
#include <QGraphicsScene>
#include <QGraphicsPixmapItem>
#include <QMessageBox>
#include <QGraphicsProxyWidget>
#include <QDebug>
#include <QDir>

// Constructor for MainWindow
MainWindow::MainWindow(QWidget *parent)
: QMainWindow(parent), ui(new Ui::MainWindow), game(new Game(this, this)) {
    ui->setupUi(this);
    previousPlayerScore = 0;
    previousComputerScore = 0;
    setupUiConnections();

    // Initialize the scenes for both game views
    QGraphicsScene *playerScene = new QGraphicsScene(this);
    ui->gameView->setScene(playerScene);

    QGraphicsScene *computerScene = new QGraphicsScene(this);
    ui->gameView_2->setScene(computerScene);

    // Set initial round label and welcome message
    ui->RoundLabel->setText("Round: 1");
    QMessageBox::information(this, "Welcome", "Welcome to the Card Game!\nPress OK to start.");

    // Set initial button text and hide gameplay buttons
    ui->startButton->setText("Start Game");
    ui->nextRoundButton->hide();
    ui->swapButton->hide();
    ui->finishGameButton->hide();
    ui->checkHandButton->hide();
}

// Destructor for MainWindow
MainWindow::~MainWindow() {
    delete ui;
}

// Method to setup UI connections
void MainWindow::setupUiConnections() {
    // Connect button clicks to corresponding methods
    connect(ui->startButton, &QPushButton::clicked, this, &MainWindow::startGame);
    connect(ui->nextRoundButton, &QPushButton::clicked, this, &MainWindow::nextRound);
    connect(ui->swapButton, &QPushButton::clicked, this, &MainWindow::swapCards);
    connect(ui->finishGameButton, &QPushButton::clicked, this, &MainWindow::finishGame);
    connect(ui->checkHandButton, &QPushButton::clicked, this, &MainWindow::checkHand);

    // Connect game signals to corresponding methods
    connect(game, &Game::scoresUpdated, this, &MainWindow::updateScores);
    connect(game, &Game::cardsUpdated, this, &MainWindow::updateCards);
    connect(game, &Game::roundWinner, this, &MainWindow::handleRoundWinner);
    connect(game, &Game::disableNextRoundButton, this, &MainWindow::disableNextRoundButton);
}

// Method to start the game
void MainWindow::startGame() {
    game->startGame();
    updateCards();
    updateRemainingCards();

    // Show gameplay buttons and hide start button
    ui->nextRoundButton->show();
    ui->swapButton->show();
    ui->checkHandButton->show();
    ui->finishGameButton->show();
    ui->startButton->hide();

    // Set initial round wins
    ui->playerRoundWins->setText("Player Round Wins: 0");
    ui->computerRoundWins->setText("Computer Round Wins: 0");
}

// Method to handle round winner
void MainWindow::handleRoundWinner(const QString &winner) {
    qDebug() << "Round Winner: " << winner;

    // Update round wins based on winner
    if (winner == "player") {
        int playerWins = previousPlayerScore + 1;
        ui->playerRoundWins->setText("Player Round Wins: " + QString::number(playerWins));
        previousPlayerScore = playerWins;  // Update to keep track
    } else if (winner == "computer") {
        int computerWins = previousComputerScore + 1;
        ui->computerRoundWins->setText("Computer Round Wins: " + QString::number(computerWins));
        previousComputerScore = computerWins;  // Update to keep track
    }
}

// Method to check the player's hand
void MainWindow::checkHand() {
    // Get the player's hand and evaluate it
    Hand playerHand = game->getPlayer1()->getHand();
    PokerHandEvaluator evaluator;
    int handValue = evaluator.evaluate(playerHand);

    // Determine the type of hand based on the hand value
    QString handType;
    switch (handValue) {
        case 9: handType = "Straight Flush"; break;
        case 8: handType = "Four of a Kind"; break;
        case 7: handType = "Full House"; break;
        case 6: handType = "Flush"; break;
        case 5: handType = "Straight"; break;
        case 4: handType = "Three of a Kind"; break;
        case 3: handType = "Two Pair"; break;
        case 2: handType = "One Pair"; break;
        default: handType = "High Card"; break;
    }

    // Display a message box with the type of hand
    QMessageBox::information(this, "Your Hand", "You have a " + handType);
}

// Method to proceed to the next round
void MainWindow::nextRound() {
    // Check the number of remaining cards
    int remainingCards = game->deck.remainingCards();

    // If there are less than 10 cards remaining, display a final round message
    if (remainingCards < 10) {
        QString message = "Final round - you are able to make ";
        if (remainingCards >= 3) {
            message += "3 more swaps. ";
        } else if (remainingCards == 2) {
            message += "2 more swaps. ";
        } else if (remainingCards == 1) {
            message += "1 more swap. ";
        } else {
            message += "no more swaps. ";
        }
        message += "Once you are happy, please select Finish Game to see the results.";
        QMessageBox::information(this, "Final Round", message);

        // Hide the next round button to prevent more rounds
        ui->nextRoundButton->hide();
        return;
    }

    // Proceed to the next round and update the UI
    game->nextRound();
    updateCards();
    updateRemainingCards();
    ui->RoundLabel->setText("Round: " + QString::number(game->getCurrentRound()));
}

// Method to finish the game
void MainWindow::finishGame() {
    // Create a result message with the round wins for each player
    QString resultMessage = "Player Round Wins: " + QString::number(previousPlayerScore) +
                            "\nComputer Round Wins: " + QString::number(previousComputerScore) + "\n";

    // Determine the overall winner and add to the result message
    if (previousPlayerScore > previousComputerScore) {
        resultMessage += "\nPlayer Wins!";
    } else if (previousComputerScore > previousPlayerScore) {
        resultMessage += "\nComputer Wins!";
    } else {
        resultMessage += "\nIt's a Draw!";
    }

    // Display the result message and reset the game
    QMessageBox::information(this, "Game Results", resultMessage);
    resetGame();
}

// Method to update the cards displayed in the UI
void MainWindow::updateCards() {
    // Clear the scenes and display the hands for each player
    QGraphicsScene *playerScene = ui->gameView->scene();
    playerScene->clear();
    displayHand(game->getPlayer1()->getHand(), 0, ui->gameView->height() - 150, true);

    QGraphicsScene *computerScene = ui->gameView_2->scene();
    computerScene->clear();
    displayHand(game->getComputerHand(), 0, 10, false);

    // Get the hand type for each player and update the UI labels
    QString playerHandType = PokerHandEvaluator().getHandType(Hand(game->getPlayer1()->getHand()));
    QString computerHandType = PokerHandEvaluator().getHandType(Hand(game->getComputerHand()));
    ui->playerHandTypeLabel->setText("Player Hand: " + playerHandType);
    ui->computerHandTypeLabel->setText("Computer Hand: " + computerHandType);
}

// Method to swap cards
void MainWindow::swapCards() {
    // Check if the player is trying to swap more than 3 cards
    if (selectedCardIndices.size() > 3 - game->swapCount) {
        QMessageBox::warning(this, "Swap Error", "You can only swap up to three cards per round.");
        return;
    }

    // Swap the selected cards
    for (int index : selectedCardIndices) {
        if (index >= 0 && index < game->getPlayer1()->getHand().size()) {
            Card newCard = game->deck.dealCard();
            newCard.setShow(true);
            game->getPlayer1()->replaceCard(index, newCard);
            game->swapCount++;
        }
    }

    // Update the scores and cards in the UI
    updateScores(game->getPlayerScore(), game->getComputerScore());
    updateCards();
    updateRemainingCards();
    clearCardSelections();
}

// Method to reset the game
void MainWindow::resetGame() {
    // Reset the game and update the UI
    game->initializeGame();
    updateCards();
    updateRemainingCards();
    ui->startButton->show();
    ui->nextRoundButton->hide();
    ui->swapButton->hide();
    ui->checkHandButton->hide();
    ui->finishGameButton->hide();
}

// Method to update the remaining cards label in the UI
void MainWindow::updateRemainingCards() {
    int remaining = game->deck.remainingCards();
    ui->RemainingCardsLabel->setText("Remaining Cards: " + QString::number(remaining));
}

// Method to update the scores in the UI
void MainWindow::updateScores(int playerScore, int computerScore) {
    ui->playerScoreLabel->setText("Player Score: " + QString::number(playerScore));
    ui->computerScoreLabel->setText("Computer Score: " + QString::number(computerScore));
}

// Method to clear the card selections
void MainWindow::clearCardSelections() {
    // Clear the list of selected card indices
    selectedCardIndices.clear();
}

// Method to display a hand of cards
void MainWindow::displayHand(const QVector<Card>& hand, qreal x, qreal y, bool isPlayer) {
    // Get the view and scene based on whether it's the player's hand or not
    QGraphicsView *view = isPlayer ? ui->gameView : ui->gameView_2;
    QGraphicsScene *scene = view->scene();
    qreal startX = x;  // Start x-coordinate

    // Loop through each card in the hand
    for (int i = 0; i < hand.size(); ++i) {
        const Card &card = hand[i];

        // Load the card image and check if it's valid
        QDir directory(QCoreApplication::applicationDirPath() + "/playing_cards");
        QPixmap image = QPixmap("playing_cards/" + card.getImagePath());
        if (image.isNull()) {
            qDebug() << "Error loading image from:" << "playing_cards/" + card.getImagePath();
            continue;
        }

        // Scale the image and create a pixmap item
        image = image.scaled(80, 120, Qt::KeepAspectRatio, Qt::SmoothTransformation);
        QGraphicsPixmapItem *item = new QGraphicsPixmapItem(image);
        item->setPos(startX, y);
        scene->addItem(item);

        // Create a label for the card and set its properties
        QGraphicsTextItem *label = scene->addText(::rankToString(static_cast<::Rank>(card.getRank())) + " of " + card.suitToString(card.getSuit()));
        label->setDefaultTextColor(Qt::white);
        QFont font = label->font();
        font.setBold(true);
        label->setFont(font);
        label->setTextWidth(80);
        label->setPos(startX, y + 125);  // Adjust y-coordinate for labels

        // If it's the player's hand, add a checkbox for card selection
        if (isPlayer) {
            QCheckBox *checkBox = new QCheckBox();
            QGraphicsProxyWidget *proxy = scene->addWidget(checkBox);
            proxy->setPos(startX, y + 160);  // Adjust y-coordinate for checkboxes
            connect(checkBox, &QCheckBox::toggled, [this, i](bool checked) {
                if (checked) {
                    selectedCardIndices.append(i);
                } else {
                    selectedCardIndices.removeAll(i);
                }
            });
        }

        startX += 100;  // Increment x-coordinate for the next card
    }
}

// Method to disable the Next Round button
void MainWindow::disableNextRoundButton() {
    // Disable the Next Round button
    ui->nextRoundButton->setEnabled(false);
}
