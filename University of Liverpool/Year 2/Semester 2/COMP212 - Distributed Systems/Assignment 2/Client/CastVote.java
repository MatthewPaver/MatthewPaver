import java.rmi.Remote;
import java.rmi.RemoteException;

public interface CastVote extends Remote {
    String requestTicket() throws RemoteException;
    void vote(String ticket, int choice) throws RemoteException;
    String getVotingResults(String ticket) throws RemoteException;
}
