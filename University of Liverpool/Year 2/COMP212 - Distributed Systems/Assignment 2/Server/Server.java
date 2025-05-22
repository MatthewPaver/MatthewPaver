import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class Server {
  public static void main(String[] args) {
    try {
      VoteImpl voteService = new VoteImpl();
      CastVote stub = (CastVote) UnicastRemoteObject.exportObject(voteService, 0);

      // Check if there is already a registry running on the default port
      Registry registry;
      try {
        registry = LocateRegistry.createRegistry(1099); // Attempt to create a new registry
        System.out.println("Java RMI registry created.");
      } catch (RemoteException e) {
        // If the registry already exists, get the existing registry
        registry = LocateRegistry.getRegistry(1099);
        System.out.println("Using existing Java RMI registry.");
      }

      registry.rebind("CastVote", stub); // Use rebind to avoid issues with rebinding
      System.out.println("Server ready");
    } catch (Exception e) {
      System.err.println("Server exception: " + e.toString());
      e.printStackTrace();
    }
  }
}