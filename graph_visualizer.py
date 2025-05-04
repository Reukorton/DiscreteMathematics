import networkx as nx
import matplotlib.pyplot as plt
from graph import Graph


class GraphVisualizer:
    @staticmethod
    def draf_graph(graph: Graph):
        """Отрисовка графа"""

        size = graph.size
        G = nx.MultiGraph()
        G.add_nodes_from(range(size))


        edges = []
        loops = {}



        for i in range(size):
            for j in range(i, size):
                weight = graph.adjacency_matrix[i, j]
                if weight > 0:
                    for k in range(weight):
                        if i == j:
                            if i not in loops:
                                loops[i] = []
                            loops[i].append((i, j))
                        else:
                            edges.append((i, j, k))

        G.add_edges_from((u, v) for u, v, _ in edges)

        pos = nx.spring_layout(G)

        colors = graph.colors
        color_map = ['lightblue', 'orange', 'green', 'red', 'purple', 'yellow', 'cyan', 'magenta']

        # Если вершины не были раскрашены, все будут серыми
        node_colors = [color_map[color % len(color_map)] if color != -1 else 'gray' for color in colors]

        nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=400)

        nx.draw_networkx_labels(G, pos, font_size=12)

        # Рисуем кратные рёбра с разными радиусами
        for i, (u, v, k) in enumerate(edges):
            rad = 0.2 + 0.1 * k
            nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], edge_color='gray', width=1.5,
                                   connectionstyle=f"arc3,rad={rad}")

        # Рисуем петли отдельно
        for node, loop_list in loops.items():
            for k, loop in enumerate(loop_list):
                rad = 0.2 + 0.1 * k
                shift_x, shift_y = 0.01 * k, 0.01 * k
                pos_shifted = {node: (pos[node][0] + shift_x, pos[node][1] + shift_y)}
                nx.draw_networkx_edges(G, pos_shifted, edgelist=[loop], edge_color='gray', width=1.5,
                                       connectionstyle=f"arc3,rad={rad}")

        plt.show()

    @staticmethod
    def color_graph(graph:Graph):
        """Простая раскраска графа 4"""
        n = graph.size
        result = [-1] * n
        result[0] = 0

        for u in range(1, n):
            used = set()
            for v in range(n):
                if graph.adjacency_matrix[u][v] > 0 and result[v] != -1:
                    used.add(result[v])
            color = 0
            while color in used:
                color += 1
            result[u] = color

        graph.colors = result
        graph.chromatic_number = max(result) + 1