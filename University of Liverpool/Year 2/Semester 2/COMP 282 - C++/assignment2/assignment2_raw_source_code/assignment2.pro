QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++17

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    card.cpp \
    deck.cpp \
    game.cpp \
    hand.cpp \
    main.cpp \
    mainwindow.cpp \
    player.cpp \
    pokerhandevaluator.cpp

HEADERS += \
    card.h \
    deck.h \
    game.h \
    hand.h \
    mainwindow.h \
    player.h \
    pokerhandevaluator.h

FORMS += \
    mainwindow.ui

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

DISTFILES += \
    ../../playing_cards/10_of_clubs.png \
    ../../playing_cards/10_of_diamonds.png \
    ../../playing_cards/10_of_hearts.png \
    ../../playing_cards/10_of_spades.png \
    ../../playing_cards/2_of_clubs.png \
    ../../playing_cards/2_of_diamonds.png \
    ../../playing_cards/2_of_hearts.png \
    ../../playing_cards/2_of_spades.png \
    ../../playing_cards/3_of_clubs.png \
    ../../playing_cards/3_of_diamonds.png \
    ../../playing_cards/3_of_hearts.png \
    ../../playing_cards/3_of_spades.png \
    ../../playing_cards/4_of_clubs.png \
    ../../playing_cards/4_of_diamonds.png \
    ../../playing_cards/4_of_hearts.png \
    ../../playing_cards/4_of_spades.png \
    ../../playing_cards/5_of_clubs.png \
    ../../playing_cards/5_of_diamonds.png \
    ../../playing_cards/5_of_hearts.png \
    ../../playing_cards/5_of_spades.png \
    ../../playing_cards/6_of_clubs.png \
    ../../playing_cards/6_of_diamonds.png \
    ../../playing_cards/6_of_hearts.png \
    ../../playing_cards/6_of_spades.png \
    ../../playing_cards/7_of_clubs.png \
    ../../playing_cards/7_of_diamonds.png \
    ../../playing_cards/7_of_hearts.png \
    ../../playing_cards/7_of_spades.png \
    ../../playing_cards/8_of_clubs.png \
    ../../playing_cards/8_of_diamonds.png \
    ../../playing_cards/8_of_hearts.png \
    ../../playing_cards/8_of_spades.png \
    ../../playing_cards/9_of_clubs.png \
    ../../playing_cards/9_of_diamonds.png \
    ../../playing_cards/9_of_hearts.png \
    ../../playing_cards/9_of_spades.png \
    ../../playing_cards/ace_of_clubs.png \
    ../../playing_cards/ace_of_diamonds.png \
    ../../playing_cards/ace_of_hearts.png \
    ../../playing_cards/ace_of_spades.png \
    ../../playing_cards/ace_of_spades2.png \
    ../../playing_cards/back.png \
    ../../playing_cards/black_joker.png \
    ../../playing_cards/jack_of_clubs.png \
    ../../playing_cards/jack_of_clubs2.png \
    ../../playing_cards/jack_of_diamonds.png \
    ../../playing_cards/jack_of_diamonds2.png \
    ../../playing_cards/jack_of_hearts.png \
    ../../playing_cards/jack_of_hearts2.png \
    ../../playing_cards/jack_of_spades.png \
    ../../playing_cards/jack_of_spades2.png \
    ../../playing_cards/king_of_clubs.png \
    ../../playing_cards/king_of_clubs2.png \
    ../../playing_cards/king_of_diamonds.png \
    ../../playing_cards/king_of_diamonds2.png \
    ../../playing_cards/king_of_hearts.png \
    ../../playing_cards/king_of_hearts2.png \
    ../../playing_cards/king_of_spades.png \
    ../../playing_cards/king_of_spades2.png \
    ../../playing_cards/queen_of_clubs.png \
    ../../playing_cards/queen_of_clubs2.png \
    ../../playing_cards/queen_of_diamonds.png \
    ../../playing_cards/queen_of_diamonds2.png \
    ../../playing_cards/queen_of_hearts.png \
    ../../playing_cards/queen_of_hearts2.png \
    ../../playing_cards/queen_of_spades.png \
    ../../playing_cards/queen_of_spades2.png
