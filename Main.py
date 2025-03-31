from Graph import Graph
from Service_Static import Service
from GraphVisualizer import GraphVisualizer

if __name__ == "__main__":
    Service.menu()
    graph = Graph(Service.get_size(), Service.get_type())
    graph.display_matrix()
    GraphVisualizer.draf_graph(graph)
    Service.display_pairs_of_sets(graph)
    Service.display_adjacency_matrix(graph)
