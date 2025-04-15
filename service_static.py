from graph import Graph
from graph_converter import GraphConverter
import numpy as np

class Service:
    @staticmethod
    def menu():
        """Вывод текстового меню для ориентации пользователя в программе"""

        print(
            "Какой граф вы хотите создать?",
            "1) Простой граф",
            "2) Полный граф",
            "3) Граф с петлями",
            "4) Граф с петлями и кратными ребрами",
            "Введите только номер графа и количество вершин",
            sep="\n"
        )

    @staticmethod
    def get_type() -> str:
        """Запрос у пользователя типа графа"""

        choice = input(
            "Тип графа: "
        ).strip()
        types = {
            "1": "simple",
            "2": "complete",
            "3": "loops",
            "4": "multi"
        }

        return types.get(choice)

    @staticmethod
    def get_size() -> int:
        """Запрос у пользователя размерность графа"""

        size = input(
            "Размерность матрицы: "
        ).strip()

        return int(size)

    @staticmethod
    def display_pairs_of_sets(graph: Graph):
        """Вывод пар множеств"""

        print(GraphConverter.converter_to_pairs_of_sets(graph))

    @staticmethod
    def display_adjacency_matrix(graph: Graph):
        """Вывод матрицы инцендентнотсти"""

        print(GraphConverter.converter_to_matrix_adjacency_matrix(graph))

    @staticmethod
    def multiplication_matrix(matrix1: np.ndarray, matrix2: np.ndarray) -> np.ndarray:
        """Перемножение матрицы на матрицу"""

        size = len(matrix1)

        matrix = np.zeros((size, size), dtype=int)

        for i in range(size):
            for j in range(size):
                for k in range(size):
                    matrix[i, j] += matrix1[i, k] * matrix2[k, j]

        return matrix

    @staticmethod
    def power_matrix(matrix: np.ndarray, power: int) -> np.ndarray:
        """Возмедение матрицы в степень power"""

        result = np.identity(len(matrix), dtype=int)
        for _ in range(power):
            result = Service.multiplication_matrix(result, matrix)

        return result


