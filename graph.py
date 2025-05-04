import numpy as np
import random
from matrix_transformation import MatrixTransformation

class Graph:
    def __init__(self, size: int, graph_type: str):
        self.size = size
        self.graph_type = graph_type
        self.adjacency_matrix = np.zeros((size, size), dtype=int)
        self.generate_graph()
        self.pairs_of_sets = \
            MatrixTransformation.converter_to_pairs_of_sets(self.adjacency_matrix)
        self.incidence_matrix = \
            MatrixTransformation.converter_to_matrix_incidence_matrix(self.adjacency_matrix)
        if graph_type == "simple" or graph_type == "complete":
            self.distance_matrix =  \
                MatrixTransformation.converter_to_matrix_distance(self.adjacency_matrix)
            self.eccentricities = MatrixTransformation.get_eccentricities(self.distance_matrix)
            self.central_vertices = MatrixTransformation.find_central_vertices(self.eccentricities)
            self.peripheral_vertices = MatrixTransformation.find_peripheral_vertices(self.eccentricities)


    def generate_graph(self):
        """Генерация матрицы смежности в зависимости от типа графа."""

        if self.graph_type == "simple":
            self.generate_graph_simple()
        elif self.graph_type == "complete":
            self.generate_graph_complete()
        elif self.graph_type == "loops":
            self.generate_graph_loops()
        elif self.graph_type == "multi":
            self.generate_graph_multi()
        else:
            raise ValueError("Неизвестный тип графа")


    def generate_graph_simple(self):
        """Генерация простого графа"""

        for i in range(self.size):
            self.adjacency_matrix[i, i] = 0

        for i in range(self.size):
            for j in range(i+1, self.size):
                self.adjacency_matrix[i, j] = self.adjacency_matrix[j, i] = random.choice([0, 1])


    def generate_graph_complete(self):
        """Генерация полного графа"""

        for i in range(self.size):
            self.adjacency_matrix[i, i] = 0

        for i in range(self.size):
            for j in range(i+1, self.size):
                self.adjacency_matrix[i, j] = self.adjacency_matrix[j, i] = 1

    def generate_graph_loops(self):
        """Генерация графа с петлями"""

        for i in range(self.size):
            self.adjacency_matrix[i, i] = random.choice([0, 1])

        for i in range(self.size):
            for j in range(i+1, self.size):
                self.adjacency_matrix[i, j] = self.adjacency_matrix[j, i] = random.choice([0, 1])

    def generate_graph_multi(self):
        """Генерация графа с петяли и кратными ребрами"""

        for i in range(self.size):
            self.adjacency_matrix[i, i] = random.choice([0, 1, 2, 3])

        for i in range(self.size):
            for j in range(i + 1, self.size):
                self.adjacency_matrix[i, j] = self.adjacency_matrix[j, i] = random.choice([0, 1, 2, 3])

    def find_max_empty_subgraph(self):
        """Поиск максимально пустого подграфа без использования networkx"""

        n = len(self.adjacency_matrix)
        selected_vertices = []

        for i in range(n):
            # Проверяем, не связан ли i с уже выбранными вершинами
            is_independent = True
            for j in selected_vertices:
                if self.adjacency_matrix[i][j] > 0 or self.adjacency_matrix[j][i] > 0:
                    is_independent = False
                    break
            if is_independent:
                selected_vertices.append(i)

        print("Максимальное пустое подмножество :", selected_vertices)
        return selected_vertices

    def color_graph(self):
        """Простая раскраска графа 4"""
        n = self.size
        result = [-1] * n
        result[0] = 0

        for u in range(1, n):
            used = set()
            for v in range(n):
                if self.adjacency_matrix[u][v] > 0 and result[v] != -1:
                    used.add(result[v])
            color = 0
            while color in used:
                color += 1
            result[u] = color

        self.colors = result
        self.chromatic_number = max(result) + 1
        print(f"Раскраска графа: {self.colors}")
        print(f"Хроматическое число графа: {self.chromatic_number}")

    def get_vertex_colors(self):
        """Вернёт цвета вершин, если они были раскрашены"""
        return getattr(self, "colors", [])