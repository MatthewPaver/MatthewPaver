public class InterfaceProcessor extends Processor {
    private final Ring subnetwork;

    public InterfaceProcessor(int id, int startRound, Ring subnetwork) {
        super(id, startRound);
        this.subnetwork = subnetwork;
    }

    @Override
    public void acknowledgeLeader(int leaderId) {
        super.acknowledgeLeader(leaderId);
        subnetwork.getProcessors().forEach(proc -> proc.acknowledgeLeader(leaderId));
    }

    public void setSubnetworkLeaderId(int leaderId) {
        subnetwork.getProcessors().forEach(proc -> proc.acknowledgeLeader(leaderId));
    }
}