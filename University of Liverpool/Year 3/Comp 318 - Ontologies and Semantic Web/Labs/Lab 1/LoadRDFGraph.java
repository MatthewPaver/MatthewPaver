import org.apache.jena.query.Dataset;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.RDFNode;
import org.apache.jena.rdf.model.Resource;
import org.apache.jena.rdf.model.Statement;
import org.apache.jena.rdf.model.StmtIterator;
import org.apache.jena.riot.RDFDataMgr;

public class LoadRDFGraph {
    public LoadRDFGraph(String fileName) {
        Dataset inputDataset = RDFDataMgr.loadDataset(fileName);
        Model model = inputDataset.getDefaultModel();

        // Print the list of statements
        StmtIterator it = model.listStatements();
        System.out.println("Prints the " + model.listStatements().toSet().size() + " triples.");

        try {
            while (it.hasNext()) {
                Statement stm = it.next();
                Resource s = stm.getSubject();
                Resource p = stm.getPredicate();
                RDFNode o = stm.getObject();
                System.out.println(s + " " + p + " " + o);
            }
        } finally {
            if (it != null) it.close();
        }
    }

    public static void main(String[] args) {
        new LoadRDFGraph("beatles.ttl");
    }
}