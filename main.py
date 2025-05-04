from graph import Graph
from service_static import Service
from graph_visualizer import GraphVisualizer

if __name__ == "__main__":
    Service.menu()
    graph = Graph(Service.get_size(), Service.get_type())
    Service.display_matrix("Матрица смежности:",
                           graph.adjacency_matrix)
    Service.display_matrix("Пары значений:",
                           graph.pairs_of_sets)
    Service.display_matrix("Матрица инциндетности:",
                           graph.incidence_matrix)
    try:
        Service.display_matrix("Матрица растояний:",
                              graph.distance_matrix)
        Service.display_matrix("Эксцентриситеты вершин:",
                               graph.eccentricities)
        Service.display_matrix("Центральные вершины:",
                               graph.central_vertices)
        Service.display_matrix("Переферийные вершины:",
                               graph.peripheral_vertices)
    except AttributeError:
        print("Матрица растояний не расчитывается для графов с петлями и кратными ребрами")

    print("\n=== ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ ===")
    graph.find_max_empty_subgraph()
    graph.color_graph()
    GraphVisualizer.draf_graph(graph)