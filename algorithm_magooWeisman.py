import numpy as np
from service_static import Service

class AlgorithmMagooWeisman:
    @staticmethod
    def creating_expression_Pl(matrix: np.ndarray) -> str:
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