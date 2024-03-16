import networkx as nx

class GraphService:
    def __init__(self):
        self.graph = self.generate_graph()

    def generate_graph(self):
        # Generate a new NetworkX graph
        graph = nx.Graph()
        # Add nodes and edges to the graph as needed
        # Example:
        graph.add_node(1)
        # adding edges implicitly adds nodes
        graph.add_edge('A', 'B', weight=4)
        graph.add_edge('B', 'C', weight=2)
        graph.add_edge('C', 'D', weight=2)
        graph.add_edge('B', 'E', weight=9)
        graph.add_edge('E', 'F', weight=1)
        graph.add_edge('F', 'G', weight=3)
        graph.add_edge('A', 'H', weight=12)
        graph.add_edge('A', 'I', weight=13)
        graph.add_edge('H', 'I', weight=0.5)
        graph.add_edge('I', 'J', weight=2)
        graph.add_edge('E', 'J', weight=50)
        return graph

    def get(self):
        # Return the graph object
        return self.graph