import java.util.Iterator;
import java.util.Scanner ;
public class Principale {

	public static void main(String[] args) {
		String regionStart;
		String regionDestination;
		
		Node dakar= new Node("DAKAR");
		Node thies = new Node("THIES");
		Node diourbel = new Node("DIOURBEL");
		Node matam = new Node("MATAM"); 
		Node kaolack = new Node("KAOLACK");
		Node kedougou = new Node("KEDOUGOU");
		Node fatick = new Node("FATICK");
		Node st_louis = new Node("SAINT-LOUIS");
		Node kolda = new Node("KOLDA");
		Node sedhiou = new Node("SEDHIOU");
		Node zig = new Node("ZIGUINCHOR");
		Node louga = new Node("LOUGA");
		Node tamba = new Node("TAMBACOUNDA");
		Node kaffrine = new Node("KAFFRINE");
		Node pikine = new Node("PIKINE");
		Node rufisque = new Node("RUFISQUE");
		

		dakar.addDestination(thies,72);
		dakar.addDestination(pikine, 13);
		pikine.addDestination(thies, 58);
		dakar.addDestination(rufisque, 29);
		rufisque.addDestination(thies, 43);
		
		dakar.addDestination(fatick,147);
		

		thies.addDestination(diourbel,89);
		thies.addDestination(louga,124);
		thies.addDestination(fatick,113);
		thies.addDestination(dakar,72);

		louga.addDestination(st_louis,74);
		louga.addDestination(matam,354);

		matam.addDestination(louga,354);
		matam.addDestination(tamba,242);
		matam.addDestination(diourbel,450);
		matam.addDestination(st_louis, 419);
		
		st_louis.addDestination(louga,74);
		st_louis.addDestination(matam,419);

		diourbel.addDestination(fatick,45);
		diourbel.addDestination(kaolack,70);
		diourbel.addDestination(kaffrine,148);
		diourbel.addDestination(matam,450);

		fatick.addDestination(kaolack,45);
		fatick.addDestination(diourbel,45);
		fatick.addDestination(dakar,147);
		
		kaolack.addDestination(kaffrine,67);
		kaolack.addDestination(zig,259);
		kaolack.addDestination(sedhiou,175);
		kaolack.addDestination(diourbel,70);
		kaolack.addDestination(fatick,45);
		
		kaffrine.addDestination(tamba,213);
		kaffrine.addDestination(diourbel,148);
		kaffrine.addDestination(kaolack,67);
		
		zig.addDestination(kolda,187);
		zig.addDestination(sedhiou,117);
		zig.addDestination(kaolack,259);
		
		
		sedhiou.addDestination(kolda,90);
		sedhiou.addDestination(kaolack,175);
		sedhiou.addDestination(zig, 117);
		
		tamba.addDestination(kedougou,234);
		tamba.addDestination(kaffrine,213);
		tamba.addDestination(matam,242);
		tamba.addDestination(kolda,226);
		
		kedougou.addDestination(tamba,234);
		kedougou.addDestination(kolda,418);
		
		
		kolda.addDestination(kedougou,418);
		kolda.addDestination(sedhiou,90);
		kolda.addDestination(tamba,226);
		kolda.addDestination(zig,187);
		kolda.addDestination(tamba,226);
		
		Graph graph = new Graph();
		
		graph.addNode(dakar);
		graph.addNode(thies);
		graph.addNode(louga);
		graph.addNode(diourbel);
		graph.addNode(fatick);
		graph.addNode(kaolack);
		graph.addNode(kaffrine);
		graph.addNode(zig);
		graph.addNode(sedhiou);
		graph.addNode(st_louis);
		graph.addNode(tamba);
		graph.addNode(kolda);
		graph.addNode(matam);
		graph.addNode(kedougou);
		
		System.out.println("De quelle region partez-vous ?");
		Scanner clavier = new Scanner(System.in);
		regionStart=clavier.nextLine();
		System.out.println("Quelle est votre destination ?");
		regionDestination=clavier.nextLine();
		clavier.close();
		
		Node destination = new Node(regionDestination);
		
		for(Node dest : graph.nodes) {
			if(destination.getName().equalsIgnoreCase(dest.getName()))
				destination=dest;
		}
		
		for(Node region : graph.nodes) {
			if(regionStart.equalsIgnoreCase(region.getName())){
				graph = Djikstra.calculateShortestPathFromSource(graph, region);
			
				for (Iterator<Node> nodes = destination.getShortestPath().iterator(); nodes.hasNext();) {
					Node node = (Node) nodes.next();
					System.out.print(node.getName()+"------>");
				}
				System.out.println(destination.getName()+": "+ destination.getDistance()+" KM\n");
			}
				
		}	
		
	}

}
