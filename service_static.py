import numpy as np
import re

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
    def display_info(*args):
        """Вывод матрицы"""
        for arg in args:
            print(arg)

    @staticmethod
    def multiplying_brackets(Pl: str) -> str:
        expressions = Pl.split(" * ")
        for i in range(len(expressions)): expressions[i] = expressions[i][1:-1].split(" + ")

        result = expressions[0]
        for i in range(1, len(expressions)):
            new_result = []
            for term in result:
                for var in expressions[i]:
                    if var not in term:
                        new_result.append(term + var)
                    else:
                        new_result.append(term)
            result = new_result

        result = set(Service.sort_summands(result))

        return result

    @staticmethod
    def sort_summands(summands: list[str]) -> list[str]:
        sorted_result = []
        for summand in summands:
            variables = [summand[i] + summand[i + 1] for i in range(0, len(summand), 2)]
            variables.sort(key=lambda x: int(x[1:]))
            sorted_result.append(''.join(variables))

        return sorted_result

    @staticmethod
    def expression_conversion(Pl: set[str]) -> set[str]:
        to_remove = set()
        parsed = {expr: set(re.findall(r'x\d+', expr)) for expr in Pl}

        for a, set_a in parsed.items():
            for b, set_b in parsed.items():
                if a != b and set_a.issubset(set_b):
                    to_remove.add(b)

        return Pl - to_remove

