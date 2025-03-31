import numpy as np
import random


class Graph:
    def __init__(self, size: int, graph_type: str):
        self.size = size  # Количество вершин
        self.graph_type = graph_type  # Тип графа
        self.adjacency_matrix = np.zeros((size, size), dtype=int)  # Инициализация матрицы смежности
        self.generate_graph()

    """Генерация матрицы смежности в зависимости от типа графа."""
    def generate_graph(self):
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

    """Генерация простого графа"""
    def generate_graph_simple(self):
        for i in range(self.size):
            self.adjacency_matrix[i, i] = 0

        for i in range(self.size):
            for j in range(i+1, self.size):
                self.adjacency_matrix[i, j] = self.adjacency_matrix[j, i] = random.choice([0, 1])

    """Генерация полного графа"""
    def generate_graph_complete(self):
        for i in range(self.size):
            self.adjacency_matrix[i, i] = 0

        for i in range(self.size):
            for j in range(i+1, self.size):
                self.adjacency_matrix[i, j] = self.adjacency_matrix[j, i] = 1

    """Генерация графа с петлями"""
    def generate_graph_loops(self):
        for i in range(self.size):
            self.adjacency_matrix[i, i] = random.choice([0, 1])

        for i in range(self.size):
            for j in range(i+1, self.size):
                self.adjacency_matrix[i, j] = self.adjacency_matrix[j, i] = random.choice([0, 1])

    """Генерация графа с петяли и кратными ребрами"""
    def generate_graph_multi(self):
        for i in range(self.size):
            self.adjacency_matrix[i, i] = random.choice([0, 1, 2, 3])

        for i in range(self.size):
            for j in range(i + 1, self.size):
                self.adjacency_matrix[i, j] = self.adjacency_matrix[j, i] = random.choice([0, 1, 2, 3])

    """Выводит матрицу смежности."""
    def display_matrix(self):
        print(self.adjacency_matrix)



