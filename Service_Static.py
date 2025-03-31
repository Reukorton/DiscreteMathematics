from Graph import Graph
from GraphConverter import GraphConverter

class Service:

    """Вывод текстового меню для ориентации пользователя в программе"""
    @staticmethod
    def menu():
        print(
            "Какой граф вы хотите создать?",
            "1) Простой граф",
            "2) Полный граф",
            "3) Граф с петлями",
            "4) Граф с петлями и кратными ребрами",
            "Введите только номер графа и количество вершин",
            sep="\n"
        )

    """Запрос у пользователя типа графа"""
    @staticmethod
    def get_type() -> str:
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

    """Запрос у пользователя размерность графа"""
    @staticmethod
    def get_size() -> int:
        size = input(
            "Размерность матрицы: "
        ).strip()

        return int(size)

    """Вывод пар множеств"""
    @staticmethod
    def display_pairs_of_sets(graph: Graph):
        print(GraphConverter.converter_to_pairs_of_sets(graph))

    """Вывод матрицы инцендентнотсти"""
    @staticmethod
    def display_adjacency_matrix(graph: Graph):
        print(GraphConverter.converter_to_matrix_adjacency_matrix(graph))


