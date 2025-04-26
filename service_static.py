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
    def display_matrix(*args):
        """Вывод матрицы"""
        for arg in args:
            print(arg)