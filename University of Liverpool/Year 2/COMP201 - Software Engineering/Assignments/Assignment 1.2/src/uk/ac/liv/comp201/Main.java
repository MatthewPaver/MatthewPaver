package uk.ac.liv.comp201;

public class Main {

    public static void main(String[] args) {
        String cardName = "coopesabc";
        Card card;

        try {
            // Create and save a new card
            Card.createNewCard(cardName);
            card = Card.loadCard(cardName);

            // Authenticator instance with the loaded card
            Authenticator authenticator = new Authenticator(card);

            // Test New Card Status (should be INVALID_CARD)
            System.out.println("New Card Fire Code Response: " + authenticator.checkFireCode("12345"));
            System.out.println("New Card Burglary Code Response: " + authenticator.checkBurglaryCode("56789"));

            // Set valid codes for the card
            card.setCodes("1234567890", "12345678");

            // Test Correct Code Entry (should be OK)
            System.out.println("Correct Fire Code Response: " + authenticator.checkFireCode("1234567890"));
            System.out.println("Correct Burglary Code Response: " + authenticator.checkBurglaryCode("12345678"));

            // Test Incorrect Code Entry (should be BAD_FIRE_CODE or BAD_BURGLARY_CODE)
            System.out.println("Incorrect Fire Code Response: " + authenticator.checkFireCode("wrongcode"));
            System.out.println("Incorrect Burglary Code Response: " + authenticator.checkBurglaryCode("wrongcode"));

            // Test Card Locking Mechanism (should eventually return CARD_LOCKED)
            for (int i = 0; i < 3; i++) {
                authenticator.checkFireCode("wrongcode");
                authenticator.checkBurglaryCode("wrongcode");
            }
            System.out.println("Locked Fire Code Response: " + authenticator.checkFireCode("1234567890"));
            System.out.println("Locked Burglary Code Response: " + authenticator.checkBurglaryCode("12345678"));

            // Test Persistence
            card = Card.loadCard(cardName);
            System.out.println("Post-reload Card Status: " + card.getCardStatus());

        } catch (CardException e) {
            e.printStackTrace();
        }
    }
}
