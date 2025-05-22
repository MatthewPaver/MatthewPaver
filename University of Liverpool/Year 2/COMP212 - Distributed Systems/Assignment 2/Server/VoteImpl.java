import java.rmi.RemoteException;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

public class VoteImpl implements CastVote {
    private final Map<Integer, Integer> votes = new HashMap<>();
    private final Map<String, Boolean> tickets = new HashMap<>();

    public VoteImpl() {
        // Initialize with 3 choices
        votes.put(1, 0);
        votes.put(2, 0);
        votes.put(3, 0);
    }

    @Override
    public String requestTicket() throws RemoteException {
        String ticket = UUID.randomUUID().toString();
        tickets.put(ticket, false);  // false indicates that the client has not voted yet
        return ticket;
    }

    @Override
    public void vote(String ticket, int choice) throws RemoteException {
        if (!tickets.containsKey(ticket) || tickets.get(ticket)) {
            throw new RemoteException("Invalid or used ticket.");
        }
        if (choice < 1 || choice > 3) {
            throw new RemoteException("Invalid choice: " + choice);
        }
        votes.put(choice, votes.getOrDefault(choice, 0) + 1);
        tickets.put(ticket, true);  // Mark the ticket as used
        System.out.println("Vote received for choice " + choice);
    }

    @Override
    public String getVotingResults(String ticket) throws RemoteException {
        if (!tickets.containsKey(ticket) || !tickets.get(ticket)) {
            throw new RemoteException("Voting results unavailable. Either the ticket is invalid or you haven't voted yet.");
        }
        return "Current voting results: " + votes.toString();
    }
}
