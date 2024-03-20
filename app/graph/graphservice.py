import random
import networkx as nx

class GraphService:
    def __init__(self):
        self.graph = self.generate_graph()

    def generate_graph(self):
        # Generate a new NetworkX graph from adjaceny list
        
        try:
            graph = nx.read_adjlist('app/graph/privatedata/graph.txt', create_using=nx.Graph(), delimiter='~')
        except:
            graph = nx.Graph()
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
    
    def get_random_node(self):
        # Return another random node from the graph with random index (not 1)
        # get node count
        node_count = len(self.graph.nodes)
        # get random index
        random_index = random.randint(1, node_count-1)
        # get node at random index
        return list(self.graph.nodes)[random_index]
    
    def save_to_file(self):
        nx.write_adjlist(self.graph, 'app/graph/privatedata/saved-graph.txt', delimiter='~')
        