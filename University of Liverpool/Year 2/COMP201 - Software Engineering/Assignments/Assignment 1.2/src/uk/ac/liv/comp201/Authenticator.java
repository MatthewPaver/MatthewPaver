package uk.ac.liv.comp201;

import static uk.ac.liv.comp201.ResponseCode.*;

public class Authenticator {
    private Card card; // this is the Card this is being checked

    public Authenticator(Card card) {
        this.card = card;
    }

    // Method to check the fire code.
    public ResponseCode checkFireCode(String passCodeFire) throws CardException {
        // Check if the card is new and return INVALID_CARD if it is.
        if (card.getStatus() == CardStatus.CARD_NEW) {
            return INVALID_CARD;
        }

        // Check if the card is locked and return CARD_LOCKED if it is.
        if (card.isLocked()) {
            return CARD_LOCKED;
        }

        // Check if the provided fire code matches the card's fire code.
        if (card.getFireCode().equals(passCodeFire)) {
            card.resetFireCodeAttempts(); // Reset the attempt count if the code is correct.
            return OK;
        } else {
            card.incrementFireCodeAttempts(); // Increment the attempt count for each wrong attempt.
            // Lock the card if the wrong code is entered 3 times and return CARD_LOCKED.
            if (card.getFireCodeAttempts() >= 3) { 
                card.lock();
                return CARD_LOCKED;
            }
            return BAD_FIRE_CODE; // Return BAD_FIRE_CODE if the code is wrong but not enough to lock the card.
        }
    }

    // Similar logic for checkBurglaryCode as for checkFireCode.
    public ResponseCode checkBurglaryCode(String passCodeBurglarCode) throws CardException {

        // Implementation similar to checkFireCode, but for burglary code.
        if (card.getStatus() == CardStatus.CARD_NEW) {
            return INVALID_CARD;
        }
        if (card.isLocked()) {
            return CARD_LOCKED;
        }
        if (card.getBurglaryCode().equals(passCodeBurglarCode)) {
            card.resetBurglaryCodeAttempts();
            return OK;
        } else {
            card.incrementBurglaryCodeAttempts();
            if (card.getBurglaryCodeAttempts() >= 3) {
                card.lock();
                return CARD_LOCKED;
            }
            return BAD_BURGLARY_CODE;
        }
    }
}
