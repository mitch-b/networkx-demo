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
        return graph

    def get(self):
        # Return the graph object
        return self.graph