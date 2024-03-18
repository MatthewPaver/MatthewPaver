
// ExperimentLogger.java
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class ExperimentLogger {
    private static final String LOG_FILE = "experiment_log.csv";
    private final BufferedWriter writer;

    public ExperimentLogger() {
        try {
            writer = new BufferedWriter(new FileWriter(LOG_FILE));
            writer.write(
                    "Main Ring Size,Subnetwork Size,Number of Subnetworks,Correct Result,Rounds,Messages\n");
        } catch (IOException e) {
            throw new RuntimeException("Failed to create log file", e);
        }
    }

    public void logExperiment(int mainRingSize, int subnetworkSize, int numSubnetworks,
            boolean isCorrect, int maxRounds, int messages) {
        if (isCorrect) {
            try {
                writer.write(String.format("%d,%d,%d,%b,%d,%d\n", mainRingSize, subnetworkSize, numSubnetworks, isCorrect, maxRounds, messages));
            } catch (IOException e) {
                System.err.println("Failed to write to log file: " + e.getMessage());
            }
        }
    }

    public void closeLogger() {
        try {
            writer.close();
        } catch (IOException e) {
            System.err.println("Failed to close log file: " + e.getMessage());
        }
    }
}