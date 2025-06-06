import numpy as np

from service_static import Service
import re

class AlgorithmMagooWeisman:
    @staticmethod
    def creating_expression_Pl(matrix: np.ndarray) -> set[str]:
        """Создание конечного Pl для алгоритма Магу-Вейсмана"""
        Pl = ""
        for i in range(len(matrix[0])):
            temp = ""
            for j in range(len(matrix)):
                if matrix[j, i] == 2:
                    continue
                if matrix[j, i] == 1:
                    temp += f"x{j} + "
            temp = temp[:-3]
            if temp not in Pl:
                Pl += f"({temp}) * "
            else:
                continue
        Pl = Pl[:-3]

        print("Изначальное выражение Pl = ", Pl)

        Pl = Service.multiplying_brackets(Pl)
        print("Выражение после раскрытия скобок Pl = ", " + ".join(Pl))

        Pl = Service.expression_conversion(Pl)
        print("Преобразованное выражение законами булевой алгебры Pl = ", " + ".join(Pl))

        return Pl


    @staticmethod
    def find_complements_for_polynomal(Pl: set[str], number_vertices: int) -> list[int]:
        """Преобразует выражения вида х0х1х2 в [0, 1, 2]"""
        subsets = []

        for expr in Pl:
            subsets.append([int(x[1:]) for x in re.findall(r"x\d+", expr)])

        complements = []
        all_vertices = set(range(number_vertices))

        for subset in subsets:
            current_set = set(subset)
            complement = list(all_vertices - current_set)
            if complement:
                complements.append(complement)

        return complements



    @staticmethod
    def chromatic_coloring_from_pl_list(complements: list[list[int]], number_vertices: int) -> list[int]:
        """Нахождение хроматического числа графа"""
        """Присвоение цвета каждой вершине графа"""
        colors = [-1] * number_vertices
        color = 0

        while complements:
            complements.sort(key=lambda s: -len(s))
            current = complements.pop(0)

            for v in current:
                if colors[v] == -1:
                    colors[v] = color

            new_subsets = []
            for sub in complements:
                new_sub = [x for x in sub if colors[x] == -1]
                if new_sub:
                    new_subsets.append(new_sub)
            complements = new_subsets

            color += 1

        return color, colors

    @staticmethod
    def get_chromatic_coloring(matrix: np.ndarray, size: int) -> tuple[int, list[int]]:
        """Использует все методы в этом классе для получения итогового результата алгоритма Магу-Вейсмана"""
        Pl = AlgorithmMagooWeisman.creating_expression_Pl(matrix)

        complements = AlgorithmMagooWeisman.find_complements_for_polynomal(Pl, size)

        chromatic_number, colors = AlgorithmMagooWeisman.chromatic_coloring_from_pl_list(complements, size)

        return chromatic_number, colors