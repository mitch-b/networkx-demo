import networkx as nx
from networkx import Graph
from app.graph.graphservice import GraphService
from pyvis.network import Network

graph_service = GraphService()

class PathService:
    def __init__(self):
        self.graphService = graph_service
    
    def get_path(self, origin: str, destination: str):
        try:
            graph = self.graphService.get()
            path = nx.shortest_path(graph, origin, destination)
            return path
        except nx.NetworkXNoPath:
            # todo: what is typical python convention for shared error contract for all services?
            return {"error": "No path between these nodes"}
    
    def visualize(self, graph: Graph):
        try:
            network = Network("500px", "500px")
            network.from_nx(graph)
            html = network.generate_html()
            return html
        except Exception as e:
            return {"error": f"Error rendering visualization: {e}"}
    
    def visualize_path(self, origin: str, destination: str):
        try:
            path = self.get_path(origin, destination)
            subgraph = self.graphService.get().subgraph(path)
            return self.visualize(subgraph)
        except:
            return {"error": "Error rendering visualization"}
        