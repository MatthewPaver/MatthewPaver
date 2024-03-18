import java.util.ArrayList;
import java.util.List;

public class RingOfRings {
    private  Ring mainRing = new Ring();
    private final List<Ring> subnetworks = new ArrayList<>();

    public void addSubnetwork(Ring subnetwork, InterfaceProcessor interfaceProcessor) {
        subnetworks.add(subnetwork);
        mainRing.addProcessor(interfaceProcessor);
    }

    public void startElection() {
        // Start the terminating LCR algorithm in each subnetwork
        subnetworks.forEach(ring -> {
            ring.setTerminating(true);
            ring.startElection();
        });

        // Start the asynchronous-start LCR algorithm in the main ring
        mainRing.setTerminating(false);
        mainRing.startElection();

        // Get the elected leader ID from the main ring
        int electedLeaderId = mainRing.getElectedLeaderId();

        // Propagate the elected leader ID to all processors in the subnetworks
        subnetworks.forEach(ring -> ring.getProcessors().forEach(proc -> proc.acknowledgeLeader(electedLeaderId)));
    }

    public Ring getMainRing() {
        return mainRing;
    }

    public int getMessageCount() {
        int messageCount = mainRing.getMessageCount();
        for (Ring subnetwork : subnetworks) {
            messageCount += subnetwork.getMessageCount();
        }
        return messageCount;
    }

    public void reset() {
        mainRing.reset();
        subnetworks.forEach(Ring::reset);
    }

    public void setMainRing(Ring mainRing2) {
        mainRing = mainRing2;
    }

    public Ring[] getSubnetworks() {
        return subnetworks.toArray(new Ring[0]);
    }
}