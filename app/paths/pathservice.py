import networkx as nx
from app.graph.graphservice import GraphService

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