from graph import Graph
from service_static import Service
from graph_visualizer import GraphVisualizer

if __name__ == "__main__":
    Service.menu()
    graph = Graph(Service.get_size(), Service.get_type())
    Service.display_matrix("Матрица смежности:",
                           graph.adjacency_matrix)
    Service.display_matrix("Матрица растояний:",
                           graph.distance_matrix)
    GraphVisualizer.draf_graph(graph)
    Service.display_matrix("Пары значений:",
                           graph.pairs_of_sets)
    Service.display_matrix("Матрица инциндетности:",
                           graph.incidence_matrix)