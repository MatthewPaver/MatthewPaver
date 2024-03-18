
// Simulator.java
import java.util.*;

public class Simulator {
    private static final int MAX_MAIN_RING_SIZE = 100; // Maximum size of the main ring for experiments
    private static final int MAX_SUBNETWORK_SIZE = 20; // Maximum size of subnetworks for experiments
    private static final int MAX_SUBNETWORKS = 10; // Maximum number of subnetworks for experiments

    private final Random random = new Random();
    private final ExperimentLogger logger = new ExperimentLogger();
    private final RingOfRings ringOfRings = new RingOfRings();

    public void runExperiments() {
        // Experiment 1: Varying main ring size with fixed subnetwork sizes and random
        // IDs
        experimentWithVaryingMainRingSize(10, 5, true);

        // Experiment 2: Varying subnetwork sizes with fixed main ring size and random
        // IDs
        experimentWithVaryingSubnetworkSizes(20, 3, true);

        // Experiment 3: Varying number of subnetworks with fixed main ring size and
        // subnetwork sizes, and ascending IDs
        experimentWithVaryingSubnetworks(30, 8, false);

        // Experiment 4: Varying main ring size with fixed subnetwork sizes and
        // ascending IDs
        experimentWithVaryingMainRingSize(15, 7, false);

        logger.closeLogger();
    }

    private void experimentWithVaryingMainRingSize(int subnetworkSize, int numSubnetworks, boolean randomIds) {
        for (int mainRingSize = 5; mainRingSize <= MAX_MAIN_RING_SIZE; mainRingSize += 5) {
            runExperimentAndLog(mainRingSize, subnetworkSize, numSubnetworks, randomIds);
        }
    }

    private void experimentWithVaryingSubnetworkSizes(int mainRingSize, int numSubnetworks, boolean randomIds) {
        for (int subnetworkSize = 3; subnetworkSize <= MAX_SUBNETWORK_SIZE; subnetworkSize += 2) {
            runExperimentAndLog(mainRingSize, subnetworkSize, numSubnetworks, randomIds);
        }
    }

    private void experimentWithVaryingSubnetworks(int mainRingSize, int subnetworkSize, boolean randomIds) {
        for (int numSubnetworks = 1; numSubnetworks <= MAX_SUBNETWORKS; numSubnetworks++) {
            runExperimentAndLog(mainRingSize, subnetworkSize, numSubnetworks, randomIds);
        }
    }

    private void runExperimentAndLog(int mainRingSize, int subnetworkSize, int numSubnetworks, boolean randomIds) {
        resetRingOfRings();
        setupRingOfRings(mainRingSize, subnetworkSize, numSubnetworks, randomIds);
        ringOfRings.startElection();

        int electedLeaderId = ringOfRings.getMainRing().getElectedLeaderId();
        int maxId = getMaxInitialId(ringOfRings);
        boolean isCorrect = electedLeaderId == maxId;
        int maxRounds = getMaxRoundsToConverge(ringOfRings); // Get the maximum rounds to converge
        int messages = ringOfRings.getMessageCount();

        logger.logExperiment(mainRingSize, subnetworkSize, numSubnetworks, isCorrect, maxRounds, messages);
    }

    private void resetRingOfRings() {
        ringOfRings.reset();
    }

    private void setupRingOfRings(int mainRingSize, int subnetworkSize, int numSubnetworks, boolean randomIds) {
        // Create main ring
        Ring mainRing = new Ring();
        for (int i = 0; i < mainRingSize; i++) {
            int id = randomIds ? random.nextInt(mainRingSize * 3) + 1 : i + 1; // Random or ascending IDs
            int startRound = 1; // All processors in the main ring start at round 1
            Processor processor = new Processor(id, startRound);
            mainRing.addProcessor(processor);
        }
        ringOfRings.setMainRing(mainRing);

        // Create subnetworks
        for (int i = 0; i < numSubnetworks; i++) {
            Ring subnetwork = new Ring();
            for (int j = 0; j < subnetworkSize; j++) {
                int id = randomIds ? random.nextInt(subnetworkSize * 3) + 1 : j + 1; // Random or ascending IDs
                int startRound = 1; // All processors in subnetworks start at round 1
                Processor processor = new Processor(id, startRound);
                subnetwork.addProcessor(processor);
            }
            int interfaceProcessorId = generateUniqueId(mainRingSize, numSubnetworks, i);
            InterfaceProcessor interfaceProcessor = new InterfaceProcessor(interfaceProcessorId, 1, subnetwork);
            ringOfRings.addSubnetwork(subnetwork, interfaceProcessor);
        }
    }
    
    private int generateUniqueId(int mainRingSize, int numSubnetworks, int subnetworkIndex) {
    int maxPossibleId = Math.max(mainRingSize * 3, numSubnetworks * MAX_SUBNETWORK_SIZE * 3);
    return maxPossibleId + subnetworkIndex + 1;
}

    private int getMaxInitialId(RingOfRings ringOfRings) {
        int maxId = Integer.MIN_VALUE;
        Ring mainRing = ringOfRings.getMainRing();
        for (Processor processor : mainRing.getProcessors()) {
            maxId = Math.max(maxId, processor.getId());
        }
        for (Ring subnetwork : ringOfRings.getSubnetworks()) {
            for (Processor processor : subnetwork.getProcessors()) {
                maxId = Math.max(maxId, processor.getId());
            }
        }
        return maxId;
    }

    private int getMaxRoundsToConverge(RingOfRings ringOfRings) {
        int maxRounds = 0;
        Ring mainRing = ringOfRings.getMainRing();
        for (Processor processor : mainRing.getProcessors()) {
            maxRounds = Math.max(maxRounds, processor.getRoundsToConverge());
        }
        for (Ring subnetwork : ringOfRings.getSubnetworks()) {
            for (Processor processor : subnetwork.getProcessors()) {
                maxRounds = Math.max(maxRounds, processor.getRoundsToConverge());
            }
        }
        return maxRounds;
    }

    public static void main(String[] args) {
        Simulator simulator = new Simulator();
        simulator.runExperiments();
    }
}