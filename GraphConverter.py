from Graph import Graph
import numpy as np

class GraphConverter:
    """Из матрицы смежности получаем пары значений"""
    @staticmethod
    def converter_to_pairs_of_sets(graph: Graph) -> []:
        pairs_of_sets = []

        for i in range(graph.size):
            for j in range(i, graph.size):
                if graph.adjacency_matrix[i, j] > 0:
                    for _ in range(graph.adjacency_matrix[i][j]):
                        pairs_of_sets.append((i, j))

        return pairs_of_sets

    """Из матрицы смедности получаем матрицу инцендетности"""
    @staticmethod
    def converter_to_matrix_adjacency_matrix(graph: Graph):
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
