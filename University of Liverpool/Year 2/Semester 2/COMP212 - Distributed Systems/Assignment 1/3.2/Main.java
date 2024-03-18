public class Main {
    public static void main(String[] args) {
        int numProcessors = 5; // Total number of processors in the ring
        Ring ringNetwork = new Ring();

        // Initialise processors with unique IDs and start rounds
        for (int i = 0; i < numProcessors; i++) {
            int startRound = i + 1; // Example start rounds
            Processor processor = new Processor(i + 1, startRound);
            ringNetwork.addProcessor(processor);
        }

        // Start the leader election process
        ringNetwork.startElection();
        System.out.println("Leader elected: Processor ID " + ringNetwork.getElectedLeaderId());
    }
}