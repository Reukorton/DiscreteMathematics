from graph import Graph
import numpy as np

class GraphConverter:
    @staticmethod
    def converter_to_pairs_of_sets(graph: Graph) -> []:
        """Из матрицы смежности получаем пары значений"""

        pairs_of_sets = []

        for i in range(graph.size):
            for j in range(i, graph.size):
                if graph.adjacency_matrix[i, j] > 0:
                    for _ in range(graph.adjacency_matrix[i][j]):
                        pairs_of_sets.append((i, j))

        return pairs_of_sets

    @staticmethod
    def converter_to_matrix_adjacency_matrix(graph: Graph):
        """Из матрицы смедности получаем матрицу инцендетности"""

        matrix = np.zeros((graph.size, len(GraphConverter.converter_to_pairs_of_sets(graph))), dtype=int)
        k = 0
        for i in range(graph.size):
            for j in range(i, graph.size):
                if graph.adjacency_matrix[i, j] > 0:
                    for _ in range(graph.adjacency_matrix[i, j]):
                        matrix[i, k] += 1
                        matrix[j, k] += 1
                        k += 1
        return matrix
