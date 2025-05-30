from graph import Graph
from service_static import Service
from graph_visualizer import GraphVisualizer

if __name__ == "__main__":
    Service.menu()
    graph = Graph(Service.get_size(), Service.get_type())
    Service.display_info("Матрица смежности:",
                           graph.adjacency_matrix)
    Service.display_info("Пары значений:",
                           graph.pairs_of_sets)
    Service.display_info("Матрица инциндетности:",
                           graph.incidence_matrix)
    Service.display_info("Хроматическое число:",
                         graph.chromatic_number)
    Service.display_info("Раскраска графа:",
                         graph.colors)

    try:
        Service.display_info("Матрица растояний:",
                              graph.distance_matrix)
        Service.display_info("Эксцентриситеты вершин:",
                               graph.eccentricities)
        Service.display_info("Центральные вершины:",
                               graph.central_vertices)
        Service.display_info("Переферийные вершины:",
                               graph.peripheral_vertices)
    except AttributeError:
        print("Матрица растояний не расчитывается для графов с петлями и кратными ребрами")

    GraphVisualizer.draf_graph(graph)