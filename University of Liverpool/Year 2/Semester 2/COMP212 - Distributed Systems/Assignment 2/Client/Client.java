import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Client {
    public static void main(String[] args) {
        try {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            CastVote stub = (CastVote) registry.lookup("CastVote");

            // Request a ticket
            String ticket = stub.requestTicket();
            System.out.println("Ticket received: " + ticket);

            // Vote using the ticket
            stub.vote(ticket, 1); // Example of voting for choice 1
            System.out.println("Voted for choice 1 with ticket " + ticket);

            // Get results using the ticket
            String results = stub.getVotingResults(ticket);
            System.out.println(results);
        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
