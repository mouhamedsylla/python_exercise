import java.util.HashSet;
import java.util.Set;

public class Graph {

    protected HashSet<Node> nodes = new HashSet<>();
    
    public void addNode(Node nodeA) {
        nodes.add(nodeA);
    }
}
