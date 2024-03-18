import java.util.ArrayList;
import java.util.List;

public class Ring {
    private final List<Processor> processors = new ArrayList<>();
    private int electedLeaderId = -1;
    private int currentRound = 1;

    // Add a processor to the ring
    public void addProcessor(Processor processor) {
        if (!processors.isEmpty()) {
            processors.get(processors.size() - 1).setClockwiseNeighbor(processor);
        }
        processors.add(processor);
    }

    // Close the ring by connecting the last and first processors
    public void closeRing() {
        if (!processors.isEmpty()) {
            processors.get(processors.size() - 1).setClockwiseNeighbor(processors.get(0));
        }
    }

    public void startElection() {
        closeRing(); // Ensure the ring is closed before starting
        boolean electionInProgress = true;

        while (electionInProgress) {
            simulateRound();
            electionInProgress = checkElectionProgress();
        }
    }

    private void simulateRound() {
        processors.forEach(p -> p.activate(currentRound));
        processors.forEach(Processor::processMessages);

        currentRound++; // Increment round for next simulation
    }

    private boolean checkElectionProgress() {
        // Check if a leader has been elected and propagate the leader ID to all processors
        for (Processor p : processors) {
            if (p.hasElected() && electedLeaderId == -1) {
                electedLeaderId = p.getLeaderId();
                processors.forEach(proc -> proc.acknowledgeLeader(electedLeaderId));
                break;
            }
        }

        // Check if all processors have acknowledged the leader
        return processors.stream().anyMatch(proc -> !proc.hasElected());
    }

    public int getElectedLeaderId() {
        return electedLeaderId;
    }
}