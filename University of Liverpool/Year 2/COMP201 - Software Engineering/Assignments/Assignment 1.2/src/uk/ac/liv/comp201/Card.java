package uk.ac.liv.comp201;

import static uk.ac.liv.comp201.ResponseCode.*;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

import uk.ac.liv.comp201.CardException;

public class Card {
    // Constants for code lengths and user ID length.
    private static final int CARD_ID_LENGTH = 9;
    private static final int MIN_FIRE_CODE_LENGTH = 10;
    private static final int MAX_FIRE_CODE_LENGTH = 14;
    private static final int MIN_BURGLARY_CODE_LENGTH = 8;
    private static final int MAX_BURGLARY_CODE_LENGTH = 10;

    // Fields to store card information and attempt counts.
    private String cardFireCode = "";
    private String cardBurlaryCode = "";
    private CardStatus cardStatus = CardStatus.CARD_NEW;
    private String cardUsername = "";

    private int fireCodeAttempts = 0;
    private int burglaryCodeAttempts = 0;

    // Constructor for Card
    public Card(String cardUsername) throws CardException {
        checkCardName(cardUsername);
        this.cardUsername = cardUsername.toLowerCase();
    }

    // Check if the card username is valid (length and alphabetic).
    private void checkCardName(String cardUsername) throws CardException {
        if (cardUsername.length() != CARD_ID_LENGTH) {
            throw new CardException(ResponseCode.INVALID_CARD_ID_LENGTH, "Invalid card ID length");
        }
        if (!cardUserNameValid(cardUsername)) {
            throw new CardException(ResponseCode.INVALID_CARD_ID, "Invalid card ID");
        }
    }

    private boolean cardUserNameValid(String cardUsername) {
        return cardUsername.chars().allMatch(Character::isAlphabetic);
    }

    // Static method to create a new card and save it.
    public static void createNewCard(String cardUsername) throws CardException {
        Card card = new Card(cardUsername);
        card.saveCard();
    }

    public String getCardFireCode() {
        return cardFireCode;
    }

    // Setters and getters for fire and burglary codes with validation.
    private void setCardFireCode(String cardFireCode) throws CardException {
        if (cardFireCode.length() < MIN_FIRE_CODE_LENGTH || cardFireCode.length() > MAX_FIRE_CODE_LENGTH || !cardFireCode.matches("[a-zA-Z0-9]+")) {
            throw new CardException(ResponseCode.INVALID_FIRE_CODE, "Invalid fire code");
        }
        this.cardFireCode = cardFireCode;
        updateCardStatus();
    }

    public String getCardBurlaryCode() {
        return cardBurlaryCode;
    }

    private void setCardBurlaryCode(String cardBurglaryCode) throws CardException {
        if (cardBurglaryCode.length() < MIN_BURGLARY_CODE_LENGTH || cardBurglaryCode.length() > MAX_BURGLARY_CODE_LENGTH || !cardBurglaryCode.matches("[0-9]+")) {
            throw new CardException(ResponseCode.INVALID_BURGLARY_CODE, "Invalid burglary code");
        }
        this.cardBurlaryCode = cardBurglaryCode;
        updateCardStatus();
    }

    // Method to update and save card status.
    private void updateCardStatus() {
        if (!this.cardFireCode.isEmpty() || !this.cardBurlaryCode.isEmpty()) {
            this.cardStatus = CardStatus.CARD_OK;
        }
        saveCard();
    }

    // Method to set both fire and burglary codes and update card status.
    public void setCodes(String cardFireCode, String cardBurglaryCode) throws CardException {
        setCardFireCode(cardFireCode);
        setCardBurlaryCode(cardBurglaryCode);
        cardStatus = CardStatus.CARD_OK;
        saveCard();
    }

    // Additional getters, setters, and logic to handle card locking and attempt counts.
    public CardStatus getCardStatus() {
        return cardStatus;
    }

    public void setCardStatus(CardStatus cardStatus) {
        this.cardStatus = cardStatus;
    }

    // Save card data to a file for persistence.
    private void saveCard() {
        try {
            FileWriter fileWriter = new FileWriter(cardUsername + ".txt");
            fileWriter.write(cardFireCode + "\n");
            fileWriter.write(cardBurlaryCode + "\n");
            fileWriter.write(cardStatus.name() + "\n");
            fileWriter.write(fireCodeAttempts + "\n");
            fileWriter.write(burglaryCodeAttempts + "\n");
            fileWriter.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // Load card data from a file.
    public static Card loadCard(String cardUsername) throws CardException {
        try {
            File file = new File(cardUsername + ".txt");
            Scanner myReader = new Scanner(file);
            Card card = new Card(cardUsername);
            if (myReader.hasNextLine()) {
                card.cardFireCode = myReader.nextLine();
            }
            if (myReader.hasNextLine()) {
                card.cardBurlaryCode = myReader.nextLine();
            }
            if (myReader.hasNextLine()) {
                card.cardStatus = CardStatus.valueOf(myReader.nextLine());
            }
            if (myReader.hasNextLine()) {
                card.fireCodeAttempts = Integer.parseInt(myReader.nextLine());
            }
            if (myReader.hasNextLine()) {
                card.burglaryCodeAttempts = Integer.parseInt(myReader.nextLine());
            }
            myReader.close();
            return card;
        } catch (FileNotFoundException e) {
            throw new CardException(CARD_NOT_FOUND, cardUsername);
        }
    }

	public CardStatus getStatus() {
        return this.cardStatus;
    }

    public boolean isLocked() {
        return this.cardStatus == CardStatus.CARD_LOCKED;
    }

    public String getFireCode() {
        return this.cardFireCode;
    }

    public void resetFireCodeAttempts() {
        this.fireCodeAttempts = 0;
    }

    public void incrementFireCodeAttempts() {
        this.fireCodeAttempts++;
    }

    public int getFireCodeAttempts() {
        return this.fireCodeAttempts;
    }

    public void lock() {
        this.cardStatus = CardStatus.CARD_LOCKED;
        saveCard(); // Save the card immediately after locking it
    }

    public String getBurglaryCode() {
        return this.cardBurlaryCode;
    }

    public void resetBurglaryCodeAttempts() {
        this.burglaryCodeAttempts = 0;
    }

    public void incrementBurglaryCodeAttempts() {
        this.burglaryCodeAttempts++;
    }

    public int getBurglaryCodeAttempts() {
        return this.burglaryCodeAttempts;
    }
}
