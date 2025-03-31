from graph import Graph
from graph_converter import GraphConverter

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


