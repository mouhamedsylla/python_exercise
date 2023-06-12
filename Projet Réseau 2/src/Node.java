import java.util.Collection;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

import java.util.Collection;
import java.util.HashMap;
import java.util.LinkedList;

public class Node {

	private String name;
    
    private java.util.List<Node> shortestPath = new LinkedList<>();
    
    private Integer distance = Integer.MAX_VALUE;
    
    HashMap<Node, Integer> adjacentNodes = new HashMap<>();

    public void addDestination(Node destination, int distance) {
        adjacentNodes.put(destination, distance);
    }
 
    public Node(String name) {
        this.name = name;
    }

	public void setDistance(int i) {
		this.distance=i;
	}

	public int getDistance() {
		return distance;
	}

	public Collection<Node> getShortestPath() {
		return shortestPath;
	}

	public void setShortestPath(LinkedList<Node> shortestPath2) {
		this.shortestPath= shortestPath2;
		
	}

	public HashMap <Node,Integer> getAdjacentNodes() {
		return  this.adjacentNodes;
	}
	
	public String getName() {
		return this.name;
	}
    
}
