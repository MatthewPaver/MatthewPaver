
// Ring.java
import java.util.ArrayList;
import java.util.List;

public class Ring {
    private final List<Processor> processors = new ArrayList<>();
    private int electedLeaderId = -1;
    private int currentRound = 1;
    private boolean isTerminating = false;


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
        // Check if a leader has been elected
        for (Processor p : processors) {
            if (p.hasElected() && electedLeaderId == -1) {
                electedLeaderId = p.getLeaderId();
                isTerminating = true; // Switch to terminating mode
                break;
            }
        }

        // In terminating mode, check if all active processors have acknowledged the
        // leader
        if (isTerminating) {
            if (allActiveProcessorsAcknowledgedLeader()) {
                return false; // Election completed
            } else {
                // Propagate the leader ID to all active processors
                processors.stream()
                        .filter(Processor::isActive)
                        .forEach(proc -> proc.acknowledgeLeader(electedLeaderId));
                return true; // Election in progress
            }
        }

        // In non-terminating mode, continue the election
        return true;
    }

    private boolean allActiveProcessorsAcknowledgedLeader() {
        return processors.stream()
                .filter(Processor::isActive)
                .allMatch(Processor::hasElected);
    }

    public int getElectedLeaderId() {
        return electedLeaderId;
    }

    public List<Processor> getProcessors() {
        return processors;
    }

    public void setTerminating(boolean terminating) {
        isTerminating = terminating;
    }

    public int getCurrentRound() {
        return currentRound;
    }

    public int getMessageCount() {
        return processors.stream().mapToInt(Processor::getMessageCount).sum();
    }

    public void reset() {
        // Reset the elected leader ID
        electedLeaderId = -1;
    }
}