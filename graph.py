import numpy as np
import random


class Graph:
    def __init__(self, size: int, graph_type: str):
        self.size = size  # Количество вершин
        self.graph_type = graph_type  # Тип графа
        self.adjacency_matrix = np.zeros((size, size), dtype=int)  # Инициализация матрицы смежности
        self.generate_graph()

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

    def display_matrix(self):
        """Выводит матрицу смежности."""

        print(self.adjacency_matrix)



