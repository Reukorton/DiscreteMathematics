import numpy as np
from service_static import Service

class MatrixTransformation:
    @staticmethod
    def converter_to_pairs_of_sets(matrix: np.ndarray) -> np.ndarray:
        """Из матрицы смежности получаем пары значений"""

        size = len(matrix)
        pairs_of_sets = []

        for i in range(size):
            for j in range(i, size):
                if matrix[i, j] > 0:
                    for _ in range(matrix[i][j]):
                        pairs_of_sets.append((i, j))

        return pairs_of_sets

    @staticmethod
    def converter_to_matrix_incidence_matrix(matrix: np.ndarray) -> np.ndarray:
        """Из матрицы смежности получаем матрицу инцендетности"""

        size = len(matrix)
        incidence_matrix = np.zeros((size, len(MatrixTransformation.converter_to_pairs_of_sets(matrix))), dtype=int)
        k = 0
        for i in range(size):
            for j in range(i, size):
                if matrix[i, j] > 0:
                    for _ in range(matrix[i, j]):
                        incidence_matrix[i, k] += 1
                        incidence_matrix[j, k] += 1
                        k += 1

        return incidence_matrix

    @staticmethod
    def converter_to_matrix_distance(matrix: np.ndarray) -> np.ndarray:
        """Из матрицы смежности в матрицу расстояний"""
        size = len(matrix)
        distances = matrix.copy()
        powered = matrix.copy()

        for power in range(2, size + 1):
            powered = Service.multiplication_matrix(powered, matrix)
            for i in range(size):
                for j in range(i + 1, size):
                    if powered[i, j] > 0 and distances[i, j] == 0:
                        distances[i, j] = distances[j, i] = power

        return distances

    @staticmethod
    def get_eccentricities(distances: np.ndarray) -> list[int]:
        """Нахождение списка инцентриситетов"""
        eccentricities = []
        for i in range(len(distances)):
            ecc = max(distances[i][j] for j in range(len(distances)) if i != j)
            eccentricities.append(ecc)

        return eccentricities

    @staticmethod
    def get_radius_and_diameter(eccentricities: list[int]) -> tuple[int, int]:
        """Нахождение радиуса и диаметра графа"""
        return min(eccentricities), max(eccentricities)

    @staticmethod
    def find_central_vertices(eccentricities: list[int]) -> list[int]:
        """Нахождение центральных вершин"""
        min_ecc = min(eccentricities)
        return [index for index, value in enumerate(eccentricities) if value == min_ecc]

    @staticmethod
    def find_peripheral_vertices(eccentricities: list[int]) -> list[int]:
        """Нахождение переферийных вершин"""
        max_ecc = max(eccentricities)
        return [index for index, value in enumerate(eccentricities) if value == max_ecc]
