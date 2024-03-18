
// Processor.java
import java.util.Queue;
import java.util.LinkedList;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.atomic.AtomicInteger;

public class Processor {
    private final int id;
    private final int startRound;
    private Processor clockwiseNeighbor;
    private final Queue<Integer> messageQueue = new LinkedList<>();
    private final AtomicBoolean isActive = new AtomicBoolean(false);
    private final AtomicBoolean hasElected = new AtomicBoolean(false);
    private int leaderId = -1;
    private final AtomicInteger messageCount = new AtomicInteger(0);
    private int roundsToConverge = 0; // New field to track rounds to converge
    private int currentRound = 1; // Current round

    public Processor(int id, int startRound) {
        this.id = id;
        this.startRound = startRound;
    }

    public void setClockwiseNeighbor(Processor neighbor) {
        this.clockwiseNeighbor = neighbor;
    }

    public void activate(int currentRound) {
        this.currentRound = currentRound; // Update the current round
        if (currentRound >= startRound && isActive.compareAndSet(false, true)) {
            // Process any messages that were received before activation but not processed
            while (!messageQueue.isEmpty()) {
                processMessage(messageQueue.poll());
            }
            sendMessage(id); // Send initial message with own ID
        }
    }

    // Send a message to the clockwise neighbor
    private void sendMessage(int message) {
        if (clockwiseNeighbor != null) {
            clockwiseNeighbor.receiveMessage(message, isActive.get());
            messageCount.incrementAndGet(); // Increment the message count
        }
    }

    // Receive a message from the counter-clockwise neighbor
    public void receiveMessage(int message, boolean senderActive) {
        if (senderActive) { // Only queue messages from active senders
            messageQueue.add(message);
        }
    }

    public void processMessages() {
        while (!messageQueue.isEmpty() && isActive.get()) {
            processMessage(messageQueue.poll());
        }
    }

    // Process the received message
    private void processMessage(int receivedId) {
        if (receivedId > id && !hasElected.get()) {
            sendMessage(receivedId);
        } else if (receivedId == id) {
            hasElected.set(true);
            leaderId = id; // Elect self and terminate
            roundsToConverge = currentRound; // Set rounds to converge
            System.out.println("Processor " + id + " elected as leader");
            // Propagate leader ID for others to terminate
            sendMessage(id);
        } else if (hasElected.get()) {
            // If this processor has already elected a leader, propagate the leader's ID
            sendMessage(leaderId);
        }
    }

    public void acknowledgeLeader(int leaderId) {
        if (!hasElected.get()) {
            this.leaderId = leaderId;
            hasElected.set(true);
            isActive.set(false); // Terminate after acknowledging the leader
            roundsToConverge = currentRound; // Set rounds to converge
            System.out.println("Processor " + id + " acknowledges leader " + leaderId);
        }
    }

    public boolean hasElected() {
        return hasElected.get();
    }

    public boolean isActive() {
        return isActive.get();
    }

    public int getId() {
        return id;
    }

    public int getLeaderId() {
        return leaderId;
    }

    public int getMessageCount() {
        return messageCount.get();
    }

    public int getRoundsToConverge() {
        return roundsToConverge;
    }
}